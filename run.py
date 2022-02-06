# Python program to demonstrate
# selenium
  
# import webdriver
from selenium import webdriver
  
# create webdriver object
driver = webdriver.Firefox()
  
# enter keyword to search
keyword = "geeksforgeeks"
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get elements
elements = driver.find_elements_by_xpath("//ul[@class ='ql-list']")

<div class="content-wrapper"><div class="item-container"><ul class="ql-list"><li class="ql-list_item"><a href="https://practice.geeksforgeeks.org/events/?ref=grb"><i class="quick-link_icon quick-link_icon-event"></i>
<span>Events at GeeksforGeeks</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://practice.geeksforgeeks.org/courses/?ref=grb"><i class="quick-link_icon quick-link_icon-course"></i>
<span>Courses at GeeksforGeeks</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://write.geeksforgeeks.org/?ref=grb"><i class="quick-link_icon quick-link_icon-article"></i>
<span>Write an Article</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://www.geeksforgeeks.org/java/?ref=grb"><i class="quick-link_icon quick-link_icon-java"></i>
<span>Java Tutorial</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://www.geeksforgeeks.org/python-programming-language/?ref=grb"><i class="quick-link_icon quick-link_icon-py"></i>
<span>Python Tutorial</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://www.geeksforgeeks.org/data-structures/?ref=grb"><i class="quick-link_icon quick-link_icon-dsa"></i>
<span>Data Structures Tutorial</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li><li class="ql-list_item"><a href="https://practice.geeksforgeeks.org/explore/?ref=grb"><i class="quick-link_icon quick-link_icon-code"></i>
<span>Coding Practice</span>
<span class="gfg-icon gfg-icon_arrow-right"></span></a></li></ul></div></div>

<div class="item-container">
<ul class="ql-list">


# rows = driver.find_elements_by_xpath("//table[@class='Level1Table']//tr[contains(@name,'hList')]")

  
# print complete elements list
print(elements)

//body[@class='blog custom-background custom-background-white']//div[@id='main']//div[@id='home-page']//div[@class='article--container_content']//dif[@class='right-top']//div[@class='side--container tutorials--container']//div[@class='card-layout']//div[@class='content-wrapper']//div[@class='item-container']



//body[@class='blog custom-background custom-background-white']
//div[@id='main']
//div[@id='home-page']
//div[@class='article--container_content']
//dif[@class='right-top']
//div[@class='side--container tutorials--container']
//div[@class='card-layout']
//div[@class='content-wrapper']
//div[@class='item-container']

ul class="ql-list">