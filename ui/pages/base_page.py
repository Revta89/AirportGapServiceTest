from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str):
        self.driver.get(url)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element(self, locator):
        """Find single element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Find multiple elements with explicit wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Click on element with explicit wait"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Send text to element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        """Check if element is displayed"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def get_text(self, locator):
        """Get text from element"""
        return self.find_element(locator).text