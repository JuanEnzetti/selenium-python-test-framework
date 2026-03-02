from pages.login_page import LoginPage
from config.settings import Settings
import allure

@allure.feature("Checkout Process")
@allure.story("Successful Purchase")
def test_complete_purchase_flow(driver):

    login_page = LoginPage(driver)
    login_page.open(Settings.BASE_URL)
    inventory_page = login_page.login(Settings.SAUCE_USERNAME, Settings.SAUCE_PASSWORD)

    with allure.step("Add product to cart"):
        inventory_page.add_product_to_cart()
        inventory_page.go_to_cart()
        inventory_page.proceed_to_checkout()

    with allure.step("Fill checkout information"):
        inventory_page.fill_checkout_info("John", "Doe", "12345")

    with allure.step("Finish order"):
        inventory_page.finish_order()
        assert inventory_page.is_order_complete(), "La compra no se completó correctamente"