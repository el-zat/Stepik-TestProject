from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, ".product_main >h1")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".col-sm-6 >p.price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 >h3>a")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-1 >p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.in:nth-child(1) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".page_inner a.btn-default")
    PRODUCT_BUTTON = (By.CSS_SELECTOR, " .product_pod h3 a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
