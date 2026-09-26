from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainShopPage:
    """Класс для работы с главной страницей магазина."""

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует главную страницу магазина.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self) -> "MainShopPage":
        """Добавляет рюкзак в корзину."""
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK)
        ).click()
        return self

    def add_bolt_tshirt(self) -> "MainShopPage":
        """Добавляет футболку Bolt T-Shirt в корзину."""
        self.driver.find_element(*self.BOLT_TSHIRT).click()
        return self

    def add_onesie(self) -> "MainShopPage":
        """Добавляет комбинезон Onesie в корзину."""
        self.driver.find_element(*self.ONESIE).click()
        return self

    def go_to_cart(self) -> "MainShopPage":
        """Переходит в корзину."""
        self.driver.find_element(*self.CART_LINK).click()
        return self
