from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу оформления заказа.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> "CheckoutPage":
        """
        Заполняет форму данными покупателя.

        :param first_name: имя.
        :param last_name: фамилия.
        :param postal_code: почтовый индекс.
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        return self

    def continue_to_overview(self) -> "CheckoutPage":
        """
        Переходит на страницу подтверждения заказа.

        :return: текущий экземпляр страницы.
        """
        self.driver.find_element(*self.CONTINUE).click()
        return self

    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: строка с итоговой суммой.
        """
        element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL)
        )
        return element.text
