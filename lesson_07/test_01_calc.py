from selenium import webdriver

from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    page.wait_for_result("15")

    assert page.get_result() == "15"

    driver.quit()
