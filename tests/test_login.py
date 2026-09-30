from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://todomvc.com/examples/angular/dist/browser/#/all")
driver.maximize_window()
#scenario: Add a new todo item
todo_text="assessment"
todo_input=wait.until(EC.element_to_be_clickable(By.XPATH,"/html/body/app-root/section/app-todo-header/header/input"))
todo_input.send_keys(todo_text)
todo_input.send_keys(Keys.ENTER)

#verify
todo_item=wait.until(EC.visibility_of_element_located(By.XPATH, "/html/body/app-root/section/app-todo-footer/footer/ul/li[2]/a']"))

assert todo_item.is_displayed()
assert todo_item.text == todo_text

#clcik the check box of to do 
checkbox =wait.until(EC.element_to_bo_clickable(By.XPATH,"/html/body/app-root/section/app-todo-list/main/ul/app-todo-item[2]/li/div/label"))
checkbox.click()

#verify the to do is completed 
todo_row=wait.until(EC.presence_of_all_elements_located(By.XPATH,f"//label[normalize-space()'{todo_text}']/parent::li"))
assert "completed" in todo_row.get_attribute("class")

#verify remaining 
counter=wait.until(EC.visibility_of_element_located(By.XPATH,"//span[contains(@class,'todo-count')]"))
print("remaining count:",counter.text)
assert "0" in counter.text


#delete todo
ActionChains(driver).move_to_element(todo_row).perform()

delete_button=wait.until(EC.element_to_be_clickable(By.XPATH,"//html/body/app-root/section/app-todo-list/main/ul/app-todo-item/li/div/button"))
delete_button.click()

#delete verification
wait.until(EC.invisibility_of_element_located(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[2]/a']"))

assert len(driver.find_elements(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[2]/a']"))==0
print("delete todo-PASS")

#filter
#add active todo

todo-input=wait.until(EC.element_to_be_clickable(By.XPATH,"/html/body/app-root/section/app-todo-header/header/input"))

todo_input.send_keys("active task")
todo_input.send_keys(Keys.ENTER)

#add another todo
odo_input=wait.until(EC.element_to_be_clickable(By.XPATH,"/html/body/app-root/section/app-todo-header/header/input"))
todo_input.send_keys("abc")
todo_input.send_keys(Keys.ENTER)

#To mark completed
completed_checkbox=wait.until(EC.element_to_be_clickble(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[3]/a"))
completed_checkbox.click()

#to check the active task

active_task=wait.until(EC.visibility_of_element_located(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[2]/a"))
assert active_task.is_displayed()


#to check the complete task is not displayed 
completed_task=driver.find_elements(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[3]/a")
assert len(completed_task)== 0
print("active filter-pass")

#completed filter
completed_button=wait.until(EC.element_to_be_clickable(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[3]/a"))
completed_button.click()

#verify the task
completed_task=wait.until(EC.visibility_of_element_located(By.XPATH,"/html/body/app-root/section/app-todo-list/main/ul/app-todo-item[3]/li/div/label"))
assert completed_task.is_displayed()

#verify the active task is not displyed
active_task=driver.find_elements(By.XPATH,"/html/body/app-root/section/app-todo-footer/footer/ul/li[2]/a")

assert len(active_task)== 0
print("Completed filter")

driver.quit()