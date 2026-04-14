from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.smartphons_page import SmartphonePage
from pages.locators import SmartphonesPageLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.order_page import OrderPage
import pytest
import allure
from data.users import TEST_USER_1
from config import BASE_URL

@pytest.mark.smoke
@pytest.mark.parametrize("run", range(1))
@allure.description("Test guest can add product to cart")
def test_guest_can_add_product_to_cart(browser, run):

    
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_katalog()
    page.should_be_katalog_word()

    cp = CatalogPage(browser, browser.current_url)
    cp.go_to_smartphone_page()
    cp.should_be_smartphone_word()

    sp = SmartphonePage(browser, browser.current_url)
    sp.select_filter(SmartphonesPageLocators.BRAND_GOOGLE)
    sp.select_filter(SmartphonesPageLocators.DATA_256)
    sp.should_be_url(
        "https://upstore24.ru/collection/phones?characteristics%5B%5D=175885426&characteristics%5B%5D=109849128"
    )
    
    sp.go_to_product_page()
    sp.should_be_description_word()

    pp = ProductPage(browser, browser.current_url)
    product_name = pp.get_product_name()
    assert "Google" in product_name, f"Нет 'Google' в названии: {product_name}"
    assert "256" in product_name, f"Нет '256' в названии: {product_name}"
    product_price = pp.get_product_price()
    pp.add_to_basket()
    pp.go_to_basket()
    pp.should_be_basket_word()

    bp = BasketPage(browser, browser.current_url)
    bp.submit_offer()

    op = OrderPage(browser, browser.current_url)
    order_product_name = op.get_order_product_name()
    order_total_price = op.get_total_price()
    expected = (product_name, product_price)
    actual = (order_product_name, order_total_price)

    assert expected == actual, f"Ожидали {expected}, получили {actual}"
   
    
    op.fill_order_form(TEST_USER_1)



# pytest -s tests\test_smoke.py --tb=line
# pytest -n 3 -s tests\test_smoke.py --tb=line
# pytest -s tests\test_smoke.py --tb=line --alluredir=allure-results
# allure serve allure-results
# pytest -m smoke -s --tb=line --alluredir=allure-results