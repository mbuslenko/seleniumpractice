# JQUERY SELECT DROPDOWN


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\ALL FOR PROGRAMMING DON'T TOUCH\chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html")

# MAIN CODE ↓
def firstlist():
    dropdown = driver.find_element_by_xpath('//*[@id="select2-country-container"]')
    sel = Select(dropdown)

    assert sel.select_by_visible_text('Australia')
    assert sel.select_by_visible_text('Bangladesh')
    assert sel.select_by_visible_text('Denmark')
    assert sel.select_by_visible_text('Hong Kong')
    assert sel.select_by_visible_text('India')
    assert sel.select_by_visible_text('Japan')
    assert sel.select_by_visible_text('Netherlands')
    assert sel.select_by_visible_text('New Zealand')
    assert sel.select_by_visible_text('South Africa')
    assert sel.select_by_visible_text('United States of America')

    print('First part was ended')


def secondlist():
    dropdown = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li/input')
    sel = Select(dropdown)

    sel.select_by_visible_text('Alabama')
    test1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[1]')

    sel.select_by_visible_text('Alaska')
    test2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[2]')

    sel.select_by_visible_text('Arizona')
    test3 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[3]')

    sel.select_by_visible_text('Arkansas')
    test4 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[4]')

    print('Second part was ended')

def thirdlist():
    dropdown = driver.find_element_by_xpath('//*[@id="select2-ve6d-container"]')
    sel = Select(dropdown)

    find1 = driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('Am')
    text1 = 'American Samoa'
    sel.select_by_visible_text(text1)

    def gettext():
        return driver.find_element_by_xpath('//*[@id="select2-ve6d-container"]').text

    if gettext() != 'American Samoa':
        print('ERROR IN thirdlist, FIELD: '+ text1)

    text2 = 'Guam'
    sel.select_by_visible_text('Guam')

    if gettext() != 'Guam':
        print('ERROR IN thirdlist, FIELD: '+ text2)

    print('Third part was ended')


def fourthlist():
    dropdown = driver.find_element_by_xpath('//*[@id="files"]')
    sel = Select(dropdown)

    assert sel.select_by_visible_text('Python')
    assert sel.select_by_visible_text('PHP')
    assert sel.select_by_visible_text('Ruby')
    assert sel.select_by_visible_text('C')
    assert sel.select_by_visible_text('Java')
    assert sel.select_by_visible_text('.NET')
    assert sel.select_by_visible_text('Unknown script')
    assert sel.select_by_visible_text('Other file')

    print('Fourth part was ended')

# INITIALIZING THE TESTS
print('-- STARTING FIRST PART')
firstlist()
print('-- STARTING SECOND PART')
secondlist()
print('-- STARTING THIRD PART')
thirdlist()
print('-- STARTING FOURTH PART')
fourthlist()
print('TESTING WAS ENDED')
# END OF THE CODE
driver.quit()
