from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://rifinder.com/")
time.sleep(3)

sign_up = driver.find_element_by_xpath("(//span[@class='elementor-button-text'])[1]").click()
time.sleep(2)
create_account = driver.find_element_by_xpath("(//p[@class='tutor-form-register-wrap'])[1]/a").click()
time.sleep(3)

first_name = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[1]/div/input").send_keys("izhar")
last_name = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[2]/div/input").send_keys("abbasi")
User_name = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[3]/div/input").send_keys('izharabbasadiii')
Email = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[4]/div/input").send_keys('izhar_abbasadi102@hotmail.com')
Password = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[5]/div/input").send_keys('12345678')
Password_confirmation = driver.find_element_by_xpath("(//div[@class='tutor-form-col-6'])[6]/div/input").send_keys('12345678')

Register = driver.find_element_by_xpath("//button[@value='register']").click()

time.sleep(10)

driver.close()

