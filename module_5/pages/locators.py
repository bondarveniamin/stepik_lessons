from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators():
    BUTTON_ADD_TO_BUCKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    SEARCH_NAME_ITEM = (By.CSS_SELECTOR, '.product_main h1')
    RESULT_NAME_ITEM = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    RESULT_PRICE_ITEM = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    SEARCH_PRICE_ITEM = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
