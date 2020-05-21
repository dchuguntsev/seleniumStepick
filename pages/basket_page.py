from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty_message_visible(self):
        basketText = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert basketText == "Ваша корзина пуста Продолжить покупки", "Корзина не пуста"

    def check_that_there_are_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)