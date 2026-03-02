import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=ROOT_DIR / ".env")

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
    SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 30