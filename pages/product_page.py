from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class productPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text

    def validate_product(self, book, price):
        bookname = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        bookprice = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert bookname == book, "Названия книг не совпадают"
        assert bookprice == price, "Цена не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
