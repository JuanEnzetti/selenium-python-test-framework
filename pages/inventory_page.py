from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")   
    
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

    def go_to_cart(self):
        self.click(self.CART_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHECKOUT_BUTTON)
        )

    def proceed_to_checkout(self):
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()

    def fill_checkout_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)