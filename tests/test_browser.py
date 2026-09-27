from selenium import webdriver
import time


def test_open_browser():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    time.sleep(5)

    assert "Google" in driver.title

    driver.quit()