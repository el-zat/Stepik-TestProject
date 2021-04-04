from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductStorePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, ".col-sm-6 >h1")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".col-sm-6 >p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class ProductBasketPageLocators():
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 >h3>a")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-1 >p")

