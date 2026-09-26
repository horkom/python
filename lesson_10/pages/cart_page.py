from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины."""

    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> "CartPage":
        """
        Нажимает кнопку оформления заказа Checkout.

        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)
        ).click()
        return self
