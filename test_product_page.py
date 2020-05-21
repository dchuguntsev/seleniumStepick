from pages.basket_page import BasketPage
from pages.product_page import productPage
from pages.login_page import LoginPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = productPage(browser, link)
    page.open()
    page.add_to_basket()
    print(page.get_price())
    print(page.get_book_name())
    assert page.validate_product(page.get_book_name(), page.get_price())

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = productPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = productPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = productPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_is_disapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = productPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = productPage(browser, link)
    page.open()
    page.go_to_login_page()
    loginPage = LoginPage(browser, browser.current_url)
    loginPage.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = productPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basketPage = BasketPage(browser, browser.current_url)
    basketPage.check_that_there_are_no_products_in_basket()
    basketPage.basket_is_empty_message_visible()


