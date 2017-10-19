# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:25:15 2017

@author: Lalith Sugavanam
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome(r'C:/Users/Lalith Mambalam/Documents/Python Scripts/Selenium/chromedriver.exe')
driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women")
# Page index used to keep track of where we are.
index = 1
#while index <= 8:
#scrape the links to all the shoes
linksLists = []
while index <= 8:
    try:
        print("Scraping tab number " + str(index))
        rankinglinks = driver.find_elements_by_xpath('.//li[@class="fadex row shoe_list rp"]//div//a[1]')
        print(len(rankinglinks))
        for i in rankinglinks:
            linkURL = i.get_attribute("href")
            linksLists.append(linkURL)
        index = index + 1
        driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women&page=" + str(index))
        time.sleep(2)
    except Exception as e:
        print(e)
        driver.close()
        break
driver.get("https://runrepeat.com/brooks-ghost-10")
time.sleep(2)

for linkURL in linksLists:
    try:
        print("scraping shoe page " + str(linkURL))
        #
        #driver.get(linkURL)
    except Exception as e:
        print(e)
        driver.close
        break