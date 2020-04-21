from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class productPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()

    def get_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".alertinner > p > strong").text

    def get_book_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".alertinner > strong").text

    def validate_product(self, book, price):
        bookname = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6 > h1").text
        bookprice = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6 > p").text
        if bookname == book and bookprice == price:
            return True
        else:
            return False
