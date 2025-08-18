from base_page import BasePage
from ui.pages.inventory_page import InventoryPage


class CartPage(BasePage):
    REMOVE_BUTTON = ("id", "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = ("id", "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)
        return self

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        return InventoryPage(self.driver)
