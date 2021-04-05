from .locators import ProductStorePageLocators
from .locators import ProductBasketPageLocators
import time
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage


class ProductStorePage(BasePage):
    def guest_can_add_product_to_basket(self):
        but_basket = self.browser.find_element(*ProductStorePageLocators.BASKET_BUTTON)
        but_basket.click()


    def get_price_and_name_in_store(self):
        product_name_in_store = self.browser.find_element(*ProductStorePageLocators.PRODUCT_NAME_IN_STORE)
        product_prise_in_store = self.browser.find_element(*ProductStorePageLocators.PRODUCT_PRICE_IN_STORE)
        return product_name_in_store.text, product_prise_in_store.text

    def check_message_about_adding_to_basket(self):
         assert self.is_element_present(*ProductStorePageLocators.SUCCESS_MESSAGE), "Success message is not presented"

class ProductBasketPage(BasePage):
    def check_price_and_name_in_basket(self, product_name_in_store, product_prise_in_store):
        product_name_in_basket = self.browser.find_element(*ProductBasketPageLocators.PRODUCT_NAME_IN_BASKET)
        product_price_in_basket = self.browser.find_element(*ProductBasketPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_name_in_store == product_name_in_basket.text, "Product name is not the same"
        assert product_prise_in_store == product_price_in_basket.text, "Product price is not the same"




