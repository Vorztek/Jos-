import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
r = requests.get("https://www.noelshack.com/admin/")


driver = webdriver.Chrome(r"C:\Users\vorzt\Documents\python\test\http\driver\chromedriver.exe")
driver.get("https://www.google.fr/")

driver.find_element_by_id("L2AGLb").click()
driver.find_element_by_name("q").send_keys("linkedin login")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text("LinkedIn Login").click()
driver.find_element_by_id("username").send_keys("theosutra34@gmail.com")
driver.find_element_by_id("password").send_keys("")
driver.find_element_by_class_name("login__form_action_container").click()
driver.find_element_by_class_name("scaling-icon").click()
print(driver.title)
#driver.find_element_by_name("btnK").click()
#driver.find_element_by_xpath("(//input[@name='jyfHyd'])[2]").click()
#driver.execute_script("window.scrollTo(0, 1080)") 
#time.sleep(5)