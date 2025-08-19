from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    BASE_URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self) -> "LoginPage":
        self.open(self.BASE_URL)
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return InventoryPage(self.driver)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
