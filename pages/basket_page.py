from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_text_about_emptyness(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_PROF), "Text about emptyness is incorrect"
