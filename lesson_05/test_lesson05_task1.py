from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    original_url = driver.current_url

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    assert "/forms/post" in driver.current_url

    driver.back()
    assert driver.current_url == original_url

    driver.quit()
