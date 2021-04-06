from TestProject.pages.product_page import ProductStorePage
from TestProject.pages.product_page import ProductBasketPage
import time
import pytest


@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6", "?promo=offer7",
                                  "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,promo):
    link1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductStorePage(browser, link1)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    name, price = page.get_price_and_name_in_store()
    link2 = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = ProductBasketPage(browser, link2)
    page.open()
    time.sleep(5)
    page.check_price_and_name_in_basket(name,price)

@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6","?promo=offer7",
                                  "?promo=offer8", "?promo=offer9"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductStorePage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_success_message_on_product_page()

@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="fix this bug")),
                                   "?promo=offer8", "?promo=offer9"])
def test_message_about_product_in_basket_is_correct(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductStorePage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    name, price = page.get_price_and_name_in_store()
    page.check_message_about_product_in_basket(name)


