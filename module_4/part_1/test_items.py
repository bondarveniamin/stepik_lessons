link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
search_button_css_locator = ".btn.btn-lg.btn-primary.btn-add-to-basket"


def test_guest_should_see_button_add_to_basket(browser):
    # Arrange
    browser.get(link)

    # Act
    answer = browser.find_element_by_css_selector(search_button_css_locator).text

    # Assert
    assert len(answer) > 0
