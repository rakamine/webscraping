# Python program to demonstrate
# selenium
  
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Firefox()
  
# enter keyword to search
keyword = "geeksforgeeks"
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get elements
# deprecated elements = driver.find_elements_by_xpath("//class[@class='ql-list_item']")
#elements = driver.find_element(By.XPATH, "(//ul[@class='ql-list'])[1]").text
print(driver.find_element_by_class_name("header-main__slider").text)

# rows = driver.find_elements_by_xpath("//table[@class='Level1Table']//tr[contains(@name,'hList')]")
#<li class="ql-list_item"><a href="https://practice.geeksforgeeks.org/events/?ref=grb"><i class="quick-link_icon quick-link_icon-event"></i>


# print complete elements list
# print(elements.text)
