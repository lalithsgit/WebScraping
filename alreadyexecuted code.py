# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:18:53 2017

@author: Lalith Mambalam
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
driver = webdriver.Chrome(r'C:/Users/Lalith Mambalam/Documents/Python Scripts/Selenium/chromedriver.exe')
#driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women")
# Page index used to keep track of where we are.
index = 1
driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women&page=")
time.sleep(3)
urlList = []
while index <= 16:
    try:
        print("Scraping tab number " + str(index))
        rankinglinks = driver.find_elements_by_xpath('.//li[@class="fadex row shoe_list rp"]//div//a[1]')
        print(len(rankinglinks))
        for i in rankinglinks:
            linkURL = i.get_attribute("href")
            urlList.append(linkURL)
        index = index + 1
        driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women&page=" + str(index))
        time.sleep(3)
    except Exception as e:
        print(e)
        driver.close()
        break
driver.close()