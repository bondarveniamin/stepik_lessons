link = "http://selenium1py.pythonanywhere.com/"
email_address = "address_qwerty_124@email.com"
password = "211385321Ven"
search_button_login_or_register = "login_link"
search_registration_email = "id_registration-email"
search_registration_password = "id_registration-password1"
search_registration_confirm_password = "id_registration-password2"
search_button_register = '[name="registration_submit"]'
search_result_text = ".alertinner.wicon"

def test_guest_register(browser):
    # Arrange
    browser.get(link)

    # Act
    browser.find_element_by_id(search_button_login_or_register).click()
    input_email_address = browser.find_element_by_id(search_registration_email).send_keys(email_address)
    input_password = browser.find_element_by_id(search_registration_password).send_keys(password)
    input_confirm_password = browser.find_element_by_id(search_registration_confirm_password).send_keys(password)
    browser.find_element_by_css_selector(search_button_register).click()
    result_title = browser.find_element_by_css_selector(search_result_text)

    # Assert
    assert len(result_title.text) > 0
