# AJAX FORM

import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/ajax-form-submit-demo.html")

# MAIN CODE ↓
name = driver.find_element_by_xpath('//*[@id="title"]').send_keys('THIS IS A PART OF AUTOMATION TESTING')
comment = driver.find_element_by_xpath('//*[@id="description"]').send_keys('THIS IS A SECOND PART OF AUTOMATION TESTING')
button = driver.find_element_by_xpath('//*[@id="btn-submit"]').click()

assert driver.find_element_by_xpath('//*[@id="submit-control"]/img')
time.sleep(3)
assert driver.find_element_by_xpath('//*[@id="submit-control"]')

print('TESTING WAS ENDED')
# END OF THE TEST
driver.quit()