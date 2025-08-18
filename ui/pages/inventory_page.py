from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.cart_page import CartPage


class InventoryPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_inventory_items_count(self) -> int:
        return len(self.find_elements(self.INVENTORY_ITEMS))

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def get_cart_badge_count(self) -> int:
        if self.is_displayed(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(self.CART_LINK)
        return CartPage(self.driver)
