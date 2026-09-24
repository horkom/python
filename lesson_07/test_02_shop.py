from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_checkout():
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    main = MainShopPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    main.add_backpack()
    main.add_bolt_tshirt()
    main.add_onesie()
    main.go_to_cart()

    cart.checkout()

    checkout.fill_form("Иван", "Петров", "123456")
    checkout.continue_to_overview()

    total = checkout.get_total()
    driver.quit()

    assert "$58.29" in total, f"Ожидали $58.29, получили: {total}"
