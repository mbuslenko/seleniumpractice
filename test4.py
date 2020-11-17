# INPUT FORM


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

# MAIN CODE ↓
firstname = input('Print the First Name')
lastname = input('Print the Second Name')
email = input('Print the email')
phone = input('Print your phone number')
address = input('Print the address')
city = input('Print a city')
zip = input('Enter a Zip code')
website = input('Print a website domain')
description = input('Enter the description of your project')
question = input('Do you have hosting? \n Print only "Yes" or "No"')

firstnameinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[1]/div/div/input').send_keys(firstname)
lastnameinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[2]/div/div/input').send_keys(lastname)
emailinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[3]/div/div/input').send_keys(email)
phoneinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[4]/div/div/input').send_keys(phone)
addressinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[5]/div/div/input').send_keys(address)
cityinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[6]/div/div/input').send_keys(city)

stateinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[7]/div/div/select')
sel = Select(stateinput)
sel.select_by_visible_text('Alabama')

zipinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[8]/div/div/input').send_keys(zip)
websiteinput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[9]/div/div/input').send_keys(website)

if question == 'Yes':
    questioninput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[10]/div/div[1]/label/input').click()
else:
    questioninput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[10]/div/div[2]/label/input').click()

descriptioninput = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[11]/div/div/textarea').send_keys(description)
send = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[13]/div/button').click()

# NEED TO PROVIDE AJAX SCANNER

# END OF THE CODE
driver.quit()