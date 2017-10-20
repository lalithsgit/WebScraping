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
import pandas as pd
driver = webdriver.Chrome(r'C:/Users/Lalith Mambalam/Documents/Python Scripts/Selenium/chromedriver.exe')
#driver.get("https://runrepeat.com/ranking/rankings-of-running-shoes?gender=women")
# Page index used to keep track of where we are.
index = 1
runnerShoeDF = pd.DataFrame()
#while index <= 8:
#scrape the links to all the shoes
runningShoeDict = {}

#"https://runrepeat.com/new-balance-860-v7")
#https://runrepeat.com/brooks-ghost-10")
csv_file = open('.\CSVFiles\RunRepeatRunningShoes.csv', 'w')
# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['Company','ShoeURL','TotalScore','TotalReviews','Discontinued','Terrain','Arch','Use','Price','ShoeWeight','ToeDrop','FootHeight','ReleaseDate','GoodSummary','BadSummary','Summary','RatingsText','FiveStars','FourStars','ThreeStars','TwoStars','OneStars'])
urlList = "https://runrepeat.com/new-balance-860-v7,https://runrepeat.com/adidas-adistar-boost-esm,https://runrepeat.com/adidas-pureboost-xpose,https://runrepeat.com/on-cloud".split(",")
for shoeURL in urlList:
    driver.get(shoeURL)
    time.sleep(5)
    totalScore = driver.find_elements_by_xpath('.//div[@class="runscore-value"]')[0].text
    totalReviews = driver.find_elements_by_xpath('//div[@class="stars-container"]/div/a')[0].text 
    companyName = driver.find_elements_by_xpath('//div[@class="aggregate_rating_wrapper"]/a/img')[0].get_attribute("alt")
    #get facts
    #check if discontinued
    try:
        itemFound =  driver.find_elements_by_xpath('//*[@id="rr_facts"]/div[2]/div[1]/div[1]')
        discontinuedShoe = "Y"
    except Exception as e:
        discontinuedShoe = "N"
    try:
        bestTerrain =  driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_terrain"]/div/div[2]/div[1]/div')[1].text
    except Exception as e:
        bestTerrain = ""
    try:
        archSupport = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_arch-support"]/div/div[2]/div[1]/div')[1].text
    except Exception as e:
        archSupport = ""
    try:
        bestUse = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_use"]/div/div[2]/div[1]/div')[1].text
    except Exception as e:
        bestUse =""
    try:
        actualPrice = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_price"]/div/div[2]/div[1]/div/span')[1].text
    except Exception as e:
        actualPrice = ""
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
        fiveStars = driver.find_elements_by_xpath('//*[@id="rcs_item_5"]/div')[2].text
    except Exception as e:
        fiveSars = ""
    try:
        fourStars = driver.find_elements_by_xpath('//*[@id="rcs_item_4"]/div')[2].text
    except Exception as e:
        fourStars = ""
    
    try:
        threeStars = driver.find_elements_by_xpath('//*[@id="rcs_item_3"]/div')[2].text
    except Exception as e:
        threeStars = ""
        
    try:
        twoStars = driver.find_elements_by_xpath('//*[@id="rcs_item_2"]/div')[2].text
    except Exception as e:
        twoStars = ""
        
    try:
        oneStars = driver.find_elements_by_xpath('//*[@id="rcs_item_1"]/div')[2].text
    except Exception as e:
        oneStars = ""
    
    try:
        clickButton = driver.find_elements_by_xpath('//i[@class="arrow"]')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight/6)")
        clickButton[0].click()
        time.sleep(1)
        shoeWeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_weight"]/div/div[2]/div[1]/div[2]/div[2]')[0].text
        heelToeDrop = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_heel-to-toe-drop"]/div/div[2]/div[1]/div[2]/div')[1].text
        foreFootHeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_forefoot-height"]/div/div[2]/div[1]/div[2]/div')[1].text
    
    except Exception as e:
        heelToeDrop = ""
        foreFootHeight = ""
    #assign values to dictionary
    runningShoeDict['Company'] = companyName
    runningShoeDict['URL'] = shoeURL
    runningShoeDict['TotalScore'] = totalScore
    runningShoeDict['TotalReviews'] = totalReviews
    runningShoeDict['Discontinued'] = discontinuedShoe
    
    runningShoeDict['Terrain'] = bestTerrain
    runningShoeDict['Arch'] = archSupport
    runningShoeDict['Use'] = bestUse
    runningShoeDict['Price'] = actualPrice
    runningShoeDict['ShoeWeight'] = shoeWeight
    runningShoeDict['ToeDrop'] = heelToeDrop
    runningShoeDict['FootHeight'] = foreFootHeight
    
    runningShoeDict['ReleaseDate'] = releaseDate
    runningShoeDict['GoodSummary'] = goodSummaryStr
    runningShoeDict['BadSummary'] = badSummaryStr
    runningShoeDict['Summary'] = aggSummaryStr
    
    runningShoeDict['RatingsText'] = ratingsText
    runningShoeDict['FiveStars'] = fiveStars
    runningShoeDict['FourStars'] = fourStars
    runningShoeDict['ThreeStars'] = threeStars
    runningShoeDict['TwoStars'] = twoStars
    runningShoeDict['OneStars'] = oneStars
    try:
        writer.writerow(runningShoeDict.values())
    except Exception as e:
        continue
#end of for loop
csv_file.close()
driver.close()