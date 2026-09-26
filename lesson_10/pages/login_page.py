from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для работы со страницей авторизации Saucedemo."""

    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу авторизации.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        """Открывает страницу авторизации."""
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполняет вход в систему.

        :param username: имя пользователя.
        :param password: пароль.
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.presence_of_element_located(self.USERNAME)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self
