# RADIO BUTTONS


import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

# MAIN CODE ↓

def FirstHalf():
    def GetCheckedValue():
        click = driver.find_element_by_xpath('//*[@id="buttoncheck"]').click()

    maleButton = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]').click()
    GetCheckedValue()
    firstCheck = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]').text
    if firstCheck == "Radio button 'Male' is checked":
        print('Male button -- Succes!')
    else:
        print('Male button -- FAILED!')

    femaleButton = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input').click()
    GetCheckedValue()
    secondCheck = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]').text
    if secondCheck == "Radio button 'Female' is checked":
        print('Female button -- Succes!')
    else:
        print('Female button -- FAILED!')


def SecondHalf():

    def MaleButton():
        maleButton = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input').click()

    def FemaleButton():
        femaleButton = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input').click()

    def zero_to_five():
        button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input').click()

    def five_to_fifteen():
        button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input').click()

    def fifteen_to_fifty():
        button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input').click()

    def GetValues():
        button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

    def Values():
        return driver.find_element_by_css_selector('p.groupradiobutton').text

    #FIRST TEST - MALE + NULL
    MaleButton()
    GetValues()
    if Values() != "Sex : Male\nAge group:":
        print('First test - FAILED!')
    else:
        print('First test - Succes!')

    #SECOND TEST - FEMALE + NULL
    FemaleButton()
    GetValues()
    if Values() != "Sex : Female\nAge group:":
        print('Second test - FAILED!')
    else:
        print('Second test - Succes!')

    #THIRD TEST - NULL + 0 to 5
    print("-- REFRESHING THE PAGE")
    driver.refresh()
    zero_to_five()
    GetValues()
    if Values() != "Sex : \nAge group: 0 - 5":
        print('Third test - FAILED!')
    else:
        print('Third test - Succes!')

    #FOURTH TEST - NULL + 5 to 15
    five_to_fifteen()
    GetValues()
    if Values() != "Sex : \nAge group: 5 - 15":
        print('Fourth test - FAILED!')
    else:
        print('Fourth test - Succes!')

    #FIFTH TEST - NULL + 15 to 50
    fifteen_to_fifty()
    GetValues()
    if Values() != "Sex : \nAge group: 15 - 50":
        print('Fifth test - FAILED!')
    else:
        print('Fifth test - Succes!')

    #SIXTH TEST - MALE + 5 to 15
    MaleButton()
    five_to_fifteen()
    if Values() != "Sex : Male\nAge group: 5 - 15":
         print('Sixth test - FAILED!')
    else:
         print('Sixth test - Succes!')

    #SEVENTH TEST - NULL + NULL
    print("-- REFRESHING THE PAGE")
    driver.refresh()
    GetValues()
    if Values() != "Sex : \nAge group:":
         print('Seventh test - FAILED!')
    else:
         print('Seventh test - Succes!')


# INITIALIZING TESTS
FirstHalf()
SecondHalf()
print('TESTING WAS ENDED')
# END OF THE CODE
driver.quit()