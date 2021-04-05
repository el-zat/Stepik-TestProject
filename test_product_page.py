from TestProject.pages.product_page import ProductStorePage
from TestProject.pages.product_page import ProductBasketPage
import time


# @pytest.mark.parametrize('link', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
#                                   "promo=offer5", "promo=offer6", "promo=offer7", "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductStorePage(browser, link1)
    page.open()
    name, price = page.get_price_and_name_in_store()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    link2 = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = ProductBasketPage(browser, link2)
    page.open()
    page.check_price_and_name_in_basket(name,price)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductStorePage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_message_about_adding_to_basket()