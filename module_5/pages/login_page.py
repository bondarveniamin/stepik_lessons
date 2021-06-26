from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Current url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Form login user name is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Form login user password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL), "Form registration email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD), "Form registration password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "Form registration password repeat is not presented"
