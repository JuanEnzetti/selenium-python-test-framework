import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=ROOT_DIR / ".env")

class Settings:
    BASE_URL = "https://www.saucedemo.com"
    SAUCE_USERNAME = "standard_user"
    SAUCE_PASSWORD = "secret_sauce"
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 30 