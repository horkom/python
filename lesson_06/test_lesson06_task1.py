from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Находим и нажимаем кнопку Start
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Ждём появления текста "Hello World!"
    hello_world = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Делаем скриншот
    driver.save_screenshot("dynamic_loading.png")

    # 5. Проверяем текст
    assert hello_world.text.strip() == "Hello World!"

    driver.quit()
