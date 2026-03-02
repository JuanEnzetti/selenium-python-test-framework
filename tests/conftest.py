import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import Settings
import os
import tempfile
import shutil
from datetime import datetime

@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_dir}")
    options.add_argument(f"--data-path={temp_dir}/data")
    options.add_argument(f"--disk-cache-dir={temp_dir}/cache")
    options.add_argument(f"--media-cache-size=0")
    options.add_argument(f"--disable-default-apps")
    
    if Settings.HEADLESS:
        options.add_argument("--headless=new")
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "enable-blink-features"])
    options.add_experimental_option("useAutomationExtension", False)
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
        "safebrowsing.forced": False,
        "password_manager_enabled": False,
        "autofill.credit_card_enabled": False,
        "autofill.profile_enabled": False,
        "browser.password_check.enabled": False,
        "browser.password_check.referrer_check_enabled": False,
        "privacy_sandbox.m1_enabled": False,
        "privacy_sandbox.first_party_sets_enabled": False,
        "content_settings.exceptions.automatic_downloads.*.setting": 1,
        "default_content_setting_values.notifications": 2,
        "default_content_settings.popups": 0,
        "managed_default_content_settings.popups": 0,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    options.add_experimental_option("prefs", prefs)
    
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck,PasswordProtection,PasswordManager,SafeBrowsingEnhancedProtection,ImprovedSecurityWarningsPhishing")
    options.add_argument("--safebrowsing-disable-auto-update")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-sync")
    options.add_argument("--metrics-recording-enabled=false")
    options.add_argument("--no-first-run")
    options.add_argument("--safebrowsing-disable-download-protection")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-domain-reliability")
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-insecure-localhost")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            })
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            })
        """
    })
    
    driver.maximize_window()
    driver.implicitly_wait(Settings.IMPLICIT_WAIT)

    yield driver

    driver.quit()
    
    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except:
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)