from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPages(BasePage):
    def add_to_bucket(self):
        search_name_item = self.browser.find_element(*ProductPageLocators.SEARCH_NAME_ITEM).text
        search_price_item = self.browser.find_element(*ProductPageLocators.SEARCH_PRICE_ITEM).text
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BUCKET)
        button.click()
        BasePage.solve_quiz_and_get_code(self)
        result_name_item = self.browser.find_element(*ProductPageLocators.RESULT_NAME_ITEM).text
        result_price_item = self.browser.find_element(*ProductPageLocators.RESULT_PRICE_ITEM).text
        assert search_name_item == result_name_item, 'Result name item is not search name item'
        assert search_price_item == result_price_item, 'Result price item is not search price item'
