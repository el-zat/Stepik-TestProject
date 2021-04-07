from TestProject.pages.product_page import ProductPage
import time
import pytest
from TestProject.pages.login_page import LoginPage
from TestProject.pages.basket_page import BasketPage

@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="this bug schould be fixed")),
                                  "?promo=offer8", "?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo):
    link1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link1)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    name, price = page.get_price_and_name_in_store()
    link2 = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = ProductPage(browser, link2)
    page.open()
    time.sleep(5)
    page.check_price_and_name_in_basket(name,price)


def test_message_about_product_in_basket_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    name, price = page.get_price_and_name_in_store()
    page.check_message_about_product_in_basket_is_correct(name)


@pytest.mark.xfail(reason="guest always sees success message after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_success_message_on_product_page_does_not_appear()


@pytest.mark.xfail(reason="success message does not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_success_message_on_product_page_disappears_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(4)
    page.check_success_message_on_product_page_does_not_appear()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.cant_see_products_in_basket()
    page.can_see_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password, browser)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(4)
        page.check_success_message_on_product_page_does_not_appear()
#
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link1)
        page.open()
        page.guest_can_add_product_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(2)
        name, price = page.get_price_and_name_in_store()
        link2 = "http://selenium1py.pythonanywhere.com/ru/basket/"
        page = ProductPage(browser, link2)
        page.open()
        time.sleep(5)
        page.check_price_and_name_in_basket(name,price)



