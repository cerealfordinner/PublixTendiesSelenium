from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.publix.com/pd/publix-chicken-tender-sub/BMO-DSB-100011")


#find and click choose store
choose_store = driver.find_element_by_class_name("cta.button")
choose_store.click()

#enter zip from search page
zip_search = driver.find_element_by_id("input_ZIPorCity,Stateorstorenumber42")
zip_search.click()
zip_search.send_keys("33309")
zip_search.send_keys(Keys.RETURN)

#assign a store after waiting for element ro present
try:
    confirm_store = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "choose-store-button.button.small"))
    )
except:
    driver.quit()
confirm_store.click()


#check of element with the class on-sale is present
try:
    on_sale = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "on-sale"))
    )
    print("On Sale!")
except:
    print("Not on Sale!")
