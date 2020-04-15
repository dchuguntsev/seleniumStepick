from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class productPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
