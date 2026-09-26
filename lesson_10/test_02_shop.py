import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Оформление заказа в Saucedemo")
@allure.description(
    "Авторизуемся, добавляем три товара в корзину, "
    "оформляем заказ и проверяем итоговую сумму $58.29."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_saucedemo_checkout():
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    main = MainShopPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открыть страницу авторизации"):
        login.open()

    with allure.step("Авторизоваться под standard_user"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить три товара в корзину"):
        main.add_backpack()
        main.add_bolt_tshirt()
        main.add_onesie()

    with allure.step("Перейти в корзину"):
        main.go_to_cart()

    with allure.step("Начать оформление заказа"):
        cart.checkout()

    with allure.step("Заполнить форму покупателя"):
        checkout.fill_form("Иван", "Петров", "123456")

    with allure.step("Перейти к подтверждению заказа"):
        checkout.continue_to_overview()

    with allure.step("Получить итоговую сумму"):
        total = checkout.get_total()

    driver.quit()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert "$58.29" in total, (
            f"Ожидали $58.29, получили: {total}"
        )
