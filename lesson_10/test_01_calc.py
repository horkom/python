import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Открываем калькулятор, ставим задержку 45 секунд, "
    "считаем 7 + 8 и проверяем, что результат равен 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Ввести выражение 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Дождаться результата 15"):
        page.wait_for_result("15")

    with allure.step("Проверить, что результат равен 15"):
        assert page.get_result() == "15"

    driver.quit()
