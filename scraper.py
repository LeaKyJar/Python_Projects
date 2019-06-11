from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set driver and open url
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.google.com.sg/search?q=rick+and+morty+memes&rlz=1C1CHBF_enSG760SG760&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjY-vC8qLThAhUH63MBHQOHACsQ_AUIDigB&biw=1536&bih=792")

# Scroll down page to load more images
for i in range(5):
    ActionChains(driver) \
        .key_down(Keys.PAGE_DOWN) \
        .key_up(Keys.PAGE_DOWN) \
        .perform()
    time.sleep(1)

# create a list of element objects
list_of_elem = driver.find_elements_by_class_name("rg_ic")
list_of_src = []

# extract src and create list of src from elem list
for i in list_of_elem:
    if i.get_attribute("src") is not None and len(list_of_src) < 100:
        list_of_src.append(i.get_attribute("src"))

# print(len(list_of_src))

# write list of src into a file
f = open("src.txt","w+")
for i in list_of_src:
    f.write(i + "\n")
f.close()