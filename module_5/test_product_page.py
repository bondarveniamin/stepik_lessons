from .pages.product_page import ProductPages
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link_2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


class TestProductPage:
    @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='')) for i in range(10)])
    def test_guest_can_add_product_to_backet_3(self, promo_offer, browser):
        browser.delete_all_cookies()
        link_3 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPages(browser, link_3)
        page.open()
        page.add_to_bucket()

    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPages(browser, link)
        page.open()
        page.add_to_bucket()

    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPages(browser, link_2)
        page.open()
        page.add_to_bucket()