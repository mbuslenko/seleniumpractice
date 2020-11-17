# CHECKBOXES


import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")


# MAIN CODE ↓
firstCheckbox = driver.find_element_by_xpath('//*[@id="isAgeSelected"]').click()
succesElement = driver.find_element_by_xpath('//*[@id="txtAge"]')
assert succesElement


def SecondTest():
    checkAllBoxes = driver.find_element_by_xpath('//*[@id="check1"]').click()
    isChecked = driver.find_element_by_xpath('//*[@id="isChkd"]')

    v = isChecked.get_attribute("value") # first condition
    if v != 'true':
        print("FAILED")
    else:
        print("succes")

    uncheckOneBox = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input').click()
    isChecked2 = driver.find_element_by_xpath('//*[@id="isChkd"]')
    if v == 'true':
        print("FAILED")
    else:
        print("SUCCES")


SecondTest()

# END OF THE TEST
driver.quit()