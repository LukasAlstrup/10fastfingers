from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

website = driver.get('https://10fastfingers.com/typing-test/english')

time.sleep(3)

allow_cookies = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
allow_cookies.click()
time.sleep(3)

while True:
    try:
        highligted_word = driver.find_element_by_class_name("highlight").text
        print(str(highligted_word))
    except:
        print("Cannot find any highlighted text!")

    try:
        driver.find_element_by_id ("inputfield").send_keys(str(highligted_word) + " ")
    except:
        print("Cannot send keystrokes to the browser!")