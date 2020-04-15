from .pages.product_page import productPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = productPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(15)
