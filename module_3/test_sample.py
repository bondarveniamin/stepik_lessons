from selenium import webdriver
import time

search_button_css_locator = ".add-to-basket button"
catalogue_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

def test_guest_should_add_item_to_basket():
    # Data
    search_name_item = "The shellcoder's handbook"
    search_button_name = "Посмотреть корзину"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(catalogue_page_link)

        # Act
        browser.find_element_by_link_text(search_name_item).click()
        browser.find_element_by_css_selector(search_button_css_locator).click()
        browser.find_element_by_link_text(search_button_name).click()

        # Assert
        result_title = browser.find_element_by_link_text(search_name_item)
        assert "The shellcoder's handbook" in result_title.text

    finally:
        browser.quit()
        
test_guest_should_add_item_to_basket()
