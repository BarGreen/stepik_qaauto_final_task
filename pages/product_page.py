from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        button.click()

    def should_be_equal_name(self):
        store_name = self.browser.find_element(*ProductPageLocators.BOOK_STORE_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_NAME).text
        assert store_name == basket_name, "Store and basket product names are not equal"

    def should_be_equal_price(self):
        store_price = self.browser.find_element(*ProductPageLocators.BOOK_STORE_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_PRICE).text
        assert store_price == basket_price, "Store and basket product prices are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared, but should be"
