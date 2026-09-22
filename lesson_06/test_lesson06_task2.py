from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


USER_1_COOKIES = [
    {
        "name": "SESSION",
        "value": "<NzlkNmRkOTUtNDM5MC00MTJkLTg1OTMtMjBhYjEzZTk4YWI5>",
        "domain": ".gitflic.ru",
        "path": "/",
    },
    {
        "name": "X-CSRF-TOKEN",
        "value": "<815d70a1-c4b5-48de-a89c-bcfbc13fcb92>",
        "domain": ".gitflic.ru",
        "path": "/",
    }
]

USER_1_PROFILE_URL = "https://gitflic.ru/user/d3a11bc57d"

USER_2_COOKIES = [
    {
        "name": "SESSION",
        "value": "<YWFhMzMxMzAtOGQxOS00MDVlLWEwODEtNGQ0YjVjOWIzYTg2>",
        "domain": ".gitflic.ru",
        "path": "/",
    },
    {
        "name": "X-CSRF-TOKEN",
        "value": "<f248a0ad-315e-498b-a3be-ea28eab3ea8f>",
        "domain": ".gitflic.ru",
        "path": "/",
    },
]

USER_2_PROFILE_URL = "https://gitflic.ru/user/cf2c558a6c"


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    for cookie in USER_1_COOKIES:
        driver.add_cookie(cookie)

    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    driver.get(USER_1_PROFILE_URL)
    WebDriverWait(driver, 10).until(
        EC.url_contains(USER_1_PROFILE_URL)
    )

    url_user_1 = driver.current_url

    driver.delete_all_cookies()
    for cookie in USER_2_COOKIES:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get(USER_2_PROFILE_URL)
    WebDriverWait(driver, 10).until(
        EC.url_contains(USER_2_PROFILE_URL)
    )

    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2

    driver.quit()
