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
        driver.find_element_by_id ("inputfield").send_keys(str(highligted_word) + " ")

        print(str(highligted_word))
    except:
        print("You made a mistake!")