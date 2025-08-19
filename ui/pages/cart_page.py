from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        super().__init__(driver)

    def remove_first_item(self) -> "CartPage":
        self.click(self.REMOVE_BUTTON)
        return self
