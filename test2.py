from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()
  
  
  
driver.get('http://www.espn.go.com')
driver.implicitly_wait(10)
print(driver.find_element_by_class_name("timestamp").text)
driver.quit()
display.stop()