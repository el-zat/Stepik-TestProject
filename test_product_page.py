from TestProject.pages.product_page import ProductStorePage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductStorePage(browser, link)
    page.open()
    name, price = page.get_price_and_name_in_store()
    page.guest_can_add_product_to_basket()
    time.sleep(2)
    page.get_price_and_name_in_store()
    page.solve_quiz_and_get_code()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductStorePage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_message_about_adding_to_basket()
