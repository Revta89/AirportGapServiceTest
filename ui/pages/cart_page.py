from ui.pages.base_page import BasePage


class CartPage(BasePage):
    REMOVE_BUTTON = ("id", "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = ("id", "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)
        return self
