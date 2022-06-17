from .pages.basket_page import BasketPage
from .pages.main_page import MainPage, LoginPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com"])
def test_guest_can_go_to_login_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_text_about_emptyness()
