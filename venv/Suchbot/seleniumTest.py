from selenium import webdriver
import time

#load Chromedriver
driver = webdriver.Chrome('C:\\Users\\Mikail\\Desktop\\Programmieren\\SuchBot\\chromedriver.exe')

#Start Website
#driver.get('https://www.google.de')
driver.get('https://www.immobilienscout24.de/')

#Maximize Window
driver.maximize_window()

#10 Seconds Wait (This is important because the Website needs to be loaded, so the button can be clicked)
driver.implicitly_wait(10)

#Find the Button and click it
#driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('wikipedia')
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

#driver.find_element_by_xpath('//*[@id="uc-center-container"]/div[3]/div/div/div/button[2]').click()
driver.find_element_by_class_name('mat-focus-indicator solo-button action-button mat-button mat-button-base mat-raised-button').click()


#search_field = driver.find_element_by_id('search')
#search_field.send_keys('iblali')
#search_field.submit()
#time.sleep(5)
#driver.quit()
