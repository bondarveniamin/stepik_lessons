from .pages.product_page import ProductPages
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
    def test_guest_can_add_product_to_backet_3(self, promo_offer, browser):
        browser.delete_all_cookies()
        link_3 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPages(browser, link_3)
        page.open()
        page.add_to_bucket()

    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPages(browser, link)
        page.open()
        # Act
        page.add_to_bucket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPages(browser, link)
        page.open()
        # Act
        page.add_to_bucket()
        # Assert
        page.should_not_success_message_after_adding_product_to_basket()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPages(browser, link)
        # Act
        page.open()
        # Assert
        page.should_not_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPages(browser, link)
        page.open()
        # Act
        page.add_to_bucket()
        # Assert
        page.should_not_message_after_adding_product_to_basket()

    @pytest.mark.skip
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPages(browser, link_2)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPages(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        # Assert
        page.should_be_login_link()
