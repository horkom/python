from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей медленного калькулятора."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку вычисления калькулятора.

        :param seconds: задержка в секундах.
        :return: текущий экземпляр страницы.
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку калькулятора по её текстовому значению.

        :param label: текст на кнопке (например, "7", "+", "=").
        :return: текущий экземпляр страницы.
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        )
        button.click()
        return self

    def wait_for_result(self, expected: str) -> "CalculatorPage":
        """
        Ожидает появления ожидаемого текста на экране калькулятора.

        :param expected: ожидаемый текст результата.
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self

    def get_result(self) -> str:
        """
        Возвращает текст результата, отображаемый на экране.

        :return: строка с результатом.
        """
        return self.driver.find_element(*self.SCREEN).text
