from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("tomsmith")
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH, '//button[@class="radius"]').click()

success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

assert "You logged into the secure area!" in success_message.text

driver.quit()