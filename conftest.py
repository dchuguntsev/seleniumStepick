import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="class")
def browser():
    print("Browser started")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(7)
    browser.quit()

