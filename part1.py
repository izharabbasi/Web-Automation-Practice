from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

download = driver.find_element_by_xpath("//a[@class='nav-item'][1]")
download.click()

search = driver.find_element_by_id("gsc-i-id1")
search.send_keys("test")
search.send_keys(Keys.RETURN)

search_results = driver.find_element_by_class_name('gsc-expansionArea')
print(search_results.text)


