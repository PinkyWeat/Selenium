import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') # this is used to ignore beign http
options.add_argument("--test-type")
driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)
actions = ActionChains(driver)


driver.get('http://www.yourWebHere.com')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nameOfClass")]'))).click()

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "theIdValueHere")))
username.clear()

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "theIdValueHere")))
password.clear()

username.send_keys("usedForLogin")
password.send_keys("usedForLogin")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "ValueGoesHere"))).click()

time.sleep(10)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "valueGoesHere")]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "valueGoesHere")]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "valueGoesHere"))).click()

megaDiv = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "valueGoesHere")]')))

time.sleep(40)

actions.move_to_element_with_offset(megaDiv, 200, 200).click().perform() # this is used to go to specific section in the screen

time.sleep(120)
