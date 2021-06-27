from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_bucket(self):
        button = self.browser.find_element(*MainPageLocators.BUCKET_BUTTON)
        button.click()

    def should_not_in_bucket_items(self):
        assert self.is_element_present(*MainPageLocators.RESULT), 'Success message is not presented'