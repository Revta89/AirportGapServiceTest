import pytest
from ui.pages.login_page import LoginPage


@pytest.fixture
def inventory_page_object(driver, creds):
    """Fixture to log in and return the inventory page object"""
    login_object = LoginPage(driver)
    return login_object.open_page().login(creds["username"], creds["password"])


@pytest.mark.ui
def test_inventory_has_six_items(inventory_page_object):
    """Verify that there are exactly 6 items on the inventory page"""
    count = inventory_page_object.get_inventory_items_count()
    assert count == 6, f"Expected 6 items, but got {count}"


@pytest.mark.ui
def test_add_first_item_to_cart(inventory_page_object):
    """Add the first item to the cart and verify the cart badge"""
    badge_count = inventory_page_object.add_first_item_to_cart().get_cart_badge_count()
    assert badge_count == 1, f"Expected cart badge 1, but got {badge_count}"
