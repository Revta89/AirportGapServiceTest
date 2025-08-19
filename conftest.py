import os
from typing import Dict
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Choose headless: True or False")
    parser.addoption('--size', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width, height')


@pytest.fixture(scope="session")
def creds() -> Dict[str, str]:
    return {
        "username": os.getenv("SAUCE_USERNAME", "standard_user"),
        "password": os.getenv("SAUCE_PASSWORD", "secret_sauce"),
    }


@pytest.fixture
def driver(request) -> WebDriver:
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()
