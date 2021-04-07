from TestProject.pages.base_page import BasePage
from TestProject.pages.locators import BasePageLocators
from TestProject.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        but_basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        but_basket.click()

    def can_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "guest can not see empty basket"

    def cant_see_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "there are products in basket but should not be"



