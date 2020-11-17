# SELECT DROPDOWN LIST


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

# MAIN CODE ↓
def firsthalf():
    dropdown = driver.find_element_by_xpath('//*[@id="select-demo"]')
    sel = Select(dropdown)

    def checkthetext():
        return driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[2]').text

    # FIRST TEST
    sel.select_by_visible_text('Sunday')
    if checkthetext() != 'Day selected :- Sunday':
        print('First test - FAILED!')
    else:
        print('First test - Succes!')

    # SECOND TEST
    sel.select_by_visible_text('Monday')
    if checkthetext() != 'Day selected :- Monday':
        print('Second test - FAILED!')
    else:
        print('Second test - Succes!')

    # THIRD TEST
    sel.select_by_visible_text('Tuesday')
    if checkthetext() != 'Day selected :- Tuesday':
        print('Third test - FAILED!')
    else:
        print('Third test - Succes!')

    # FOURTH TEST
    sel.select_by_visible_text('Wednesday')
    if checkthetext() != 'Day selected :- Wednesday':
        print('Fourth test - FAILED!')
    else:
        print('Fourth test - Succes!')

    # FIFTH TEST
    sel.select_by_visible_text('Thursday')
    if checkthetext() != 'Day selected :- Thursday':
        print('Fifth test - FAILED!')
    else:
        print('Fifth test - Succes!')

    # SIXTH TEST
    sel.select_by_visible_text('Friday')
    if checkthetext() != 'Day selected :- Friday':
        print('Sixth test - FAILED!')
    else:
        print('Sixth test - Succes!')

    # SIXTH TEST
    sel.select_by_visible_text('Saturday')
    if checkthetext() != 'Day selected :- Saturday':
        print('Seventh test - FAILED!')
    else:
        print('Seventh test - Succes!')


def secondhalf():
    list = driver.find_element_by_xpath('//*[@id="multi-select"]')
    sel = Select(list)

    def checkthetext():
        button = driver.find_element_by_xpath('//*[@id="printAll"]').click()
        return driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text

    # FIRST TEST
    sel.select_by_visible_text('California')
    if checkthetext() != 'Options selected are : California':
        print('First test - FAILED!')
    else:
        print('First test - Succes!')

    # SECOND TEST
    sel.select_by_visible_text('Florida')
    if checkthetext() != 'Options selected are : Florida':
        print('Second test - FAILED!')
    else:
        print('Second test - Succes!')

    # THIRD TEST
    sel.select_by_visible_text('New Jersey')
    if checkthetext() != 'Options selected are : New Jersey':
        print('Third test - FAILED!')
    else:
        print('Third test - Succes!')

    # FOURTH TEST
    sel.select_by_visible_text('New York')
    if checkthetext() != 'Options selected are : New York':
        print('Fourth test - FAILED!')
    else:
        print('Fourth test - Succes!')

    # FIFTH TEST
    sel.select_by_visible_text('Ohio')
    if checkthetext() != 'Options selected are : Ohio':
        print('Fifth test - FAILED!')
    else:
        print('Fifth test - Succes!')

    # SIXTH TEST
    sel.select_by_visible_text('Texas')
    if checkthetext() != 'Options selected are : Texas':
        print('Sixth test - FAILED!')
    else:
        print('Sixth test - Succes!')

    # SEVENTH TEST
    sel.select_by_visible_text('Pennsylvania')
    if checkthetext() != 'Options selected are : Pennsylvania':
        print('Seventh test - FAILED!')
    else:
        print('Seventh test - Succes!')

    # EIGHTH TEST
    sel.select_by_visible_text('Washington')
    if checkthetext() != 'Options selected are : Washington':
        print('Eighth test - FAILED!')
    else:
        print('Eighth test - Succes!')


# INITIALIZING TESTS
print('-- Starting first half...')
firsthalf()
print('-- Starting second half...')
secondhalf()
print('TESTING WAS ENDED')
# END OF THE CODE
driver.quit()