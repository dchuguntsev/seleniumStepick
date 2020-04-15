import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    print("Browser started")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

