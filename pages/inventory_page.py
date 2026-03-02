from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)