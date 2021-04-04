from TestProject.pages.locators import ProductStorePageLocators
from TestProject.pages.locators import ProductBasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
from TestProject.pages.base_page import BasePage


class ProductStorePage(BasePage):
    def guest_can_add_product_to_basket(self):
        but_basket = self.browser.find_element(*ProductStorePageLocators.BASKET_BUTTON)
        but_basket.click()

    def get_price_and_name_in_store(self):
        product_name_in_store = self.browser.find_element(*ProductStorePageLocators.PRODUCT_NAME_IN_STORE)
        product_prise_in_store = self.browser.find_element(*ProductStorePageLocators.PRODUCT_PRICE_IN_STORE)
        return product_name_in_store.text, product_prise_in_store.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = float(str(math.log(abs((12 * math.sin(float(x)))))))
        alert.send_keys("answer")
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_message_about_adding_to_basket(self):
        assert self.is_element_present(*ProductStorePageLocators.SUCCESS_MESSAGE), "Success message is presented"


class ProductBasketPage(BasePage):
    def check_price_and_name_in_basket(self, product_name_in_store, product_prise_in_store):
        product_name_in_basket = self.browser.find_element(*ProductBasketPageLocators.PRODUCT_NAME_IN_BASKET)
        product_price_in_basket = self.browser.find_element(*ProductBasketPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_name_in_store == product_name_in_basket.text, "Product name is not the same"
        assert product_prise_in_store == product_price_in_basket.text, "Price is wrong"




