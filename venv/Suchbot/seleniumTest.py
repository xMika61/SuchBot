from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# load Chromedriver
driver = webdriver.Chrome('C:\\Users\\Mikail\\Desktop\\Repository\\SuchBot\\chromedriver.exe')

# Start Website
# driver.get('https://www.google.de')
driver.get('https://www.immobilienscout24.de/')

# Maximize Window
driver.maximize_window()

# Find the Button and click it
# driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()
# driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('wikipedia')
# driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

driver.implicitly_wait(60)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="gdpr-consent-notice"]'))
WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save"]'))).click()
#driver.find_element_by_xpath('//*[@id="save"]').click()

driver.implicitly_wait(20)


ortFeld = driver.find_element_by_xpath('//*[@id="oss-location"]')
ortFeld.send_keys('50226')
driver.implicitly_wait(5)
preisFeld = driver.find_element_by_xpath('//*[@id="oss-price"]')
preisFeld.send_keys('900')
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="oss-form"]/article/div/div[3]/button').click()
#driver.find_element_by_xpath('//*[@id="captcha-box"]/div/div[2]/div[1]/div[3]').click()
kaltmiete = driver.find_element_by_class_name('font-highlight font-tabular')
driver.implicitly_wait(10)
if kaltmiete < 900 in driver.page_source:
    print('1 Angebot')
else:
    driver.close()

#angebot = driver.find_element_by_xpath('//*[@id="result-l-127357442"]/div/div[2]/div/div[5]/div[1]/dl[1]/dd')


print('1 Angebot')

#driver.find_element_by_xpath('//*[@id="oss-form"]/article/div/div[3]/button').click()

driver.implicitly_wait(60)

# search_field = driver.find_element_by_id('search')
# search_field.send_keys('iblali')
# search_field.submit()
# time.sleep(5)
# driver.quit()
