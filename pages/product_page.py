from TestProject.pages.locators import ProductPageLocators
from TestProject.pages.base_page import BasePage


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        but_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        but_basket.click()

    def get_price_and_name_in_store(self):
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        return product_name_in_store.text, product_prise_in_store.text

    def check_message_about_product_in_basket_is_correct(self,product_name_in_store):
        message_prod_in_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name_in_store == message_prod_in_basket.text, "book name in message is wrong"

    def check_success_message_on_product_page_appears(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def check_success_message_on_product_page_does_not_appear(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented/"\
                                                                                       "but it schould not be"
    def check_success_message_on_product_page_disappears_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message does not diassaper"

    def check_price_and_name_in_basket(self, product_name_in_store, product_prise_in_store):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_name_in_store == product_name_in_basket.text, "Product name is not the same"
        assert product_prise_in_store == product_price_in_basket.text, "Product price is not the same"




