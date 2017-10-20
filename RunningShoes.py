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
#driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women")
# Page index used to keep track of where we are.
index = 1
#while index <= 8:
#scrape the links to all the shoes

driver.get("https://runrepeat.com/adidas-adistar-boost-esm")
#"https://runrepeat.com/new-balance-860-v7")
#https://runrepeat.com/brooks-ghost-10")
time.sleep(4)

totalScore = driver.find_elements_by_xpath('.//div[@class="runscore-value"]')[0].text
totalReviews = driver.find_elements_by_xpath('//div[@class="stars-container"]/div/a')[0].text 
companyName = driver.find_elements_by_xpath('//div[@class="aggregate_rating_wrapper"]/a/img')[0].get_attribute("alt")
#click on show more facts item

#get facts
#check if discontinued
try:
    itemFound =  driver.find_elements_by_xpath('//*[@id="rr_facts"]/div[2]/div[1]/div[1]')
    discontinuedShoe = "Y"
except Exception as e:
    discontinuedShoe = "N"
bestTerrain =  driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_terrain"]/div/div[2]/div[1]/div')[1].text
archSupport = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_arch-support"]/div/div[2]/div[1]/div')[1].text
bestUse = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_use"]/div/div[2]/div[1]/div')[1].text
actualPrice = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_price"]/div/div[2]/div[1]/div/span')[1].text
#check if there is a release date
try:
    releaseDate = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_release-date"]/div/div[2]/div[1]/div')[1].text
except Exception as e:
    releaseDate = ""
#get reviews
try:
    goodSummaryStr=""
    txtList =  driver.find_elements_by_xpath('//*[@id="the_good"]/div/div/ul/li')
    for txt in txtList:
        goodSummaryStr += txt.text +";"
except Exception as e:
    goodSummaryStr = ""
try:
    badSummaryStr = ""
    txtList =  driver.find_elements_by_xpath('//*[@id="the_bad"]/div/div/ul/li')
    for txt in txtList:
        badSummaryStr += txt.text +";"
except Exception as e:
    badSummaryStr = ""
try:
    aggSummaryStr = ""
    aggSummaryStr =  driver.find_elements_by_xpath('//*[@id="bottom_line"]/div/div/div/p')[1].text
    for txt in txtList:
        aggSummaryStr += txt.text +";"
except Exception as e:
    aggSummaryStr = ""
ratingsText = driver.find_elements_by_xpath('//*[@id="rr_rating"]/div/div/p')[0].text
try:
    fiveSars = driver.find_elements_by_xpath('//*[@id="rcs_item_5"]/div')[2].text
    fourStars = driver.find_elements_by_xpath('//*[@id="rcs_item_4"]/div')[2].text
    threeStars = driver.find_elements_by_xpath('//*[@id="rcs_item_3"]/div')[2].text
    twoStars = driver.find_elements_by_xpath('//*[@id="rcs_item_2"]/div')[2].text
    oneStars = driver.find_elements_by_xpath('//*[@id="rcs_item_1"]/div')[2].text
except Exception as e:
    fiveSars = ""
driver.execute("window.scrollTo(0,7)")
try:
    clickButton = driver.find_elements_by_xpath('//i[@class="arrow"]')
    clickButton[0].click()
    time.sleep(3)
    showWeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_weight"]/div/div[2]/div[1]/div[2]/div[2]')[0].text
    heelToeDrop = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_heel-to-toe-drop"]/div/div[2]/div[1]/div[2]/div')[1].text
    foreFootHeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_forefoot-height"]/div/div[2]/div[1]/div[2]/div')[1].text
except Exception as e:
    heelToeDrop = ""
    foreFootHeight = ""