# SIMPLE FORMS

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # to make it easier to select items
import time

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
print('START WAITING...')
time.sleep(5)
print('WAITING ENDED!')

# MAIN CODE ↓

closeTheAd = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]').click() # Close the ad

text = 'THIS IS A PART OF AUTOMATION TESTING'

inputText = driver.find_element(By.ID, "user-message").send_keys(text) # Input text
pressTheButton = driver.find_element_by_css_selector('[onclick="showInput();"]').click() # Show our text

textElement = driver.find_element_by_xpath('//*[@id="display"]').text
# print("Inputed text: " + textElement) | TypeError: can only concatenate str (not "WebElement") to str


firstValue = 4
secondValue = 7

inputFirstValue = driver.find_element_by_xpath('//*[@id="sum1"]').send_keys(firstValue)
inputSecondValue = driver.find_element_by_xpath('//*[@id="sum2"]').send_keys(secondValue)
getTotal = driver.find_element_by_css_selector('[onclick="return total()"]').click()

valueElement = driver.find_element_by_xpath('//*[@id="displayvalue"]').text
intValueElement = int(valueElement)

# CHECKING THE TESTS
print('##########################')
if text == textElement:
    print("1 TEST PASSED")

trueValue = firstValue + secondValue
if intValueElement == trueValue:
    print("2 TEST PASSED")

print('##########################')
print("TESTS WERE ENDED")
# END OF THE CODE
driver.quit()
