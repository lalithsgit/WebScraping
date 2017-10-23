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

csv_file = open('./CSVFiles/runshoe4.csv', 'w')
# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
#urlList = ['https://runrepeat.com/brooks-ghost-10','https://runrepeat.com/adidas-ultra-boost-uncaged']#, 'https://runrepeat.com/new-balance-860-v7']#, 'https://runrepeat.com/adidas-adistar-boost-esm', 'https://runrepeat.com/adidas-tracerocker', 'https://runrepeat.com/adidas-ultra-boost-x', 'https://runrepeat.com/salomon-speedcross-4-cs', 'https://runrepeat.com/puma-ignite-evoknit', 'https://runrepeat.com/adidas-adizero-boston-boost', 'https://runrepeat.com/on-cloudflow', 'https://runrepeat.com/salomon-kalalau', 'https://runrepeat.com/nike-air-zoom-pegasus-34', 'https://runrepeat.com/nike-flyknit-racer', 'https://runrepeat.com/brooks-cascadia-12', 'https://runrepeat.com/brooks-revel', 'https://runrepeat.com/mizuno-wave-rider-20', 'https://runrepeat.com/adidas-terrex-swift-r-gtx', 'https://runrepeat.com/brooks-caldera', 'https://runrepeat.com/asics-33-m', 'https://runrepeat.com/asics-gel-noosa-tri-11', 'https://runrepeat.com/skechers-flex-appeal-2-0', 'https://runrepeat.com/asics-dynaflyte', 'https://runrepeat.com/adidas-vigor-6-tr', 'https://runrepeat.com/asics-gel-sendai', 'https://runrepeat.com/nike-air-zoom-vomero-12', 'https://runrepeat.com/merrell-bare-access-arc', 'https://runrepeat.com/merrell-crush-light', 'https://runrepeat.com/on-cloud', 'https://runrepeat.com/new-balance-990-v4', 'https://runrepeat.com/adidas-pureboost-xpose', 'https://runrepeat.com/merrell-all-out-crush', 'https://runrepeat.com/brooks-launch-4', 'https://runrepeat.com/inov-8-mudclaw-300', 'https://runrepeat.com/asics-gel-kayano-24', 'https://runrepeat.com/on-cloudsurfer', 'https://runrepeat.com/new-balance-vazee-rush-v2', 'https://runrepeat.com/asics-gel-kinsei', 'https://runrepeat.com/brooks-purecadence-6', 'https://runrepeat.com/on-cloudflyer', 'https://runrepeat.com/under-armour-speedform-apollo', 'https://runrepeat.com/hoka-one-one-tor-ultra-hi-wp', 'https://runrepeat.com/adidas-ultra-boost', 'https://runrepeat.com/brooks-glycerin-15', 'https://runrepeat.com/altra-escalante', 'https://runrepeat.com/adidas-response-boost', 'https://runrepeat.com/new-balance-840', 'https://runrepeat.com/adidas-terrex-agravic-speed', 'https://runrepeat.com/brooks-adrenaline-gts-17', 'https://runrepeat.com/nike-lunarstelos', 'https://runrepeat.com/puma-carson-runner', 'https://runrepeat.com/asics-gel-quantum-180-2', 'https://runrepeat.com/nike-fs-lite-run-4', 'https://runrepeat.com/new-balance-vazee-prism-v2', 'https://runrepeat.com/adidas-ultra-boost-st', 'https://runrepeat.com/armour-speedform-fortis-vent', 'https://runrepeat.com/mizuno-wave-inspire-13', 'https://runrepeat.com/adidas-supernova', 'https://runrepeat.com/under-armour-dash-rn-2', 'https://runrepeat.com/skechers-gorun-5', 'https://runrepeat.com/asics-gel-venture-6', 'https://runrepeat.com/nike-air-zoom-elite-9', 'https://runrepeat.com/brooks-pureflow-6', 'https://runrepeat.com/la-sportiva-mutant', 'https://runrepeat.com/salomon-speedcross-4-gtx', 'https://runrepeat.com/inov-8-x-talon-212', 'https://runrepeat.com/saucony-shadow-6000', 'https://runrepeat.com/brooks-transcend-4', 'https://runrepeat.com/saucony-breakthru', 'https://runrepeat.com/asics-gel-evate', 'https://runrepeat.com/salomon-speedcross-4', 'https://runrepeat.com/puma-tazon-6-mesh', 'https://runrepeat.com/armour-micro-g-assert-6', 'https://runrepeat.com/nike-flex-fury-2', 'https://runrepeat.com/asics-gel-contend-4', 'https://runrepeat.com/puma-ignite', 'https://runrepeat.com/adidas-alphabounce-engineered-mesh', 'https://runrepeat.com/nike-lunarepic-flyknit', 'https://runrepeat.com/asics-gel-quantum-360', 'https://runrepeat.com/saucony-ride-10', 'https://runrepeat.com/hoka-one-one-valor', 'https://runrepeat.com/new-balance-610', 'https://runrepeat.com/adidas-powerblaze', 'https://runrepeat.com/adidas-element-refine-tricot', 'https://runrepeat.com/puma-ignite-disc', 'https://runrepeat.com/nike-lunarepic-low-flyknit-2', 'https://runrepeat.com/salomon-sonic-pro', 'https://runrepeat.com/salomon-x-scream-foil', 'https://runrepeat.com/nike-free-rn', 'https://runrepeat.com/nike-air-zoom-winflo-4', 'https://runrepeat.com/adidas-adizero-takumi-sen', 'https://runrepeat.com/inov-8-x-talon-200', 'https://runrepeat.com/salomon-x-mission-3', 'https://runrepeat.com/adidas-alphabounce', 'https://runrepeat.com/nike-downshifter-7', 'https://runrepeat.com/brooks-addiction', 'https://runrepeat.com/saucony-echelon', 'https://runrepeat.com/hoka-one-one-arahi', 'https://runrepeat.com/saucony-peregrine-7', 'https://runrepeat.com/armour-charged-bandit-2', 'https://runrepeat.com/new-balance-1210-v3', 'https://runrepeat.com/hoka-one-one-gaviota', 'https://runrepeat.com/asics-gel-foundation', 'https://runrepeat.com/nike-lunartempo', 'https://runrepeat.com/asics-patriot-8', 'https://runrepeat.com/merrell-all-out-crush-tough-mudder', 'https://runrepeat.com/merrell-pace-glove', 'https://runrepeat.com/saucony-xodus-iso-runshield', 'https://runrepeat.com/salomon-xa-pro-3d-gtx', 'https://runrepeat.com/nike-flex-experience-rn-6', 'https://runrepeat.com/salomon-speedcross-vario', 'https://runrepeat.com/saucony-freedom-iso', 'https://runrepeat.com/merrell-all-out-charge', 'https://runrepeat.com/inov-8-roclite-282-gtx', 'https://runrepeat.com/adidas-terrex-x-king', 'https://runrepeat.com/skechers-gorun-400', 'https://runrepeat.com/saucony-omni-15', 'https://runrepeat.com/nike-free-rn-flyknit-2017', 'https://runrepeat.com/adidas-terrex-agravic', 'https://runrepeat.com/nike-zoom-all-out-low', 'https://runrepeat.com/brooks-puregrit-6', 'https://runrepeat.com/asics-gel-surveyor-5', 'https://runrepeat.com/nike-air-max-sequent-2', 'https://runrepeat.com/adidas-terrex-skychaser', 'https://runrepeat.com/puma-ignite-mesh', 'https://runrepeat.com/saucony-lancer', 'https://runrepeat.com/merrell-all-out-peak', 'https://runrepeat.com/saucony-cohesion-10', 'https://runrepeat.com/adidas-vengeful', 'https://runrepeat.com/adidas-energy-cloud', 'https://runrepeat.com/inov-8-terraclaw-220', 'https://runrepeat.com/hoka-one-one-bondi-5', 'https://runrepeat.com/nike-lunar-skyelux', 'https://runrepeat.com/newton-distance-elite', 'https://runrepeat.com/adidas-terrex-fast-r-gtx', 'https://runrepeat.com/vibram-fivefingers-kso-evo', 'https://runrepeat.com/armour-fat-tire-gtx', 'https://runrepeat.com/adidas-energy-boost', 'https://runrepeat.com/saucony-kineta-relay', 'https://runrepeat.com/adidas-alphabounce-ams', 'https://runrepeat.com/asics-gel-sonoma-3', 'https://runrepeat.com/newton-motion', 'https://runrepeat.com/nike-air-zoom-span', 'https://runrepeat.com/hoka-one-one-clifton-4', 'https://runrepeat.com/asics-gel-exalt', 'https://runrepeat.com/la-sportiva-akasha', 'https://runrepeat.com/nike-lunarglide-9', 'https://runrepeat.com/adidas-adizero-adios-boost', 'https://runrepeat.com/salomon-x-scream-3d', 'https://runrepeat.com/armour-speedform-slingshot', 'https://runrepeat.com/hoka-one-one-valor-ltr', 'https://runrepeat.com/adidas-duramo-lite', 'https://runrepeat.com/vibram-fivefingers-v-run', 'https://runrepeat.com/puma-ignite-pwrwarm', 'https://runrepeat.com/inov-8-roclite-305', 'https://runrepeat.com/vibram-fivefingers-kmd-sport', 'https://runrepeat.com/merrell-vapor-glove', 'https://runrepeat.com/adidas-mana-bounce-2', 'https://runrepeat.com/new-balance-fresh-foam-zante-v3', 'https://runrepeat.com/mizuno-synchro-mx', 'https://runrepeat.com/la-sportiva-ultra-raptor', 'https://runrepeat.com/vibram-fivefingers-spyridon-mr', 'https://runrepeat.com/salomon-speedcross-pro', 'https://runrepeat.com/nike-air-zoom-structure-20', 'https://runrepeat.com/inov-8-x-claw-275', 'https://runrepeat.com/salomon-xa-pro-3d-cs-wp', 'https://runrepeat.com/new-balance-880-v7', 'https://runrepeat.com/la-sportiva-wildcat-gtx', 'https://runrepeat.com/armour-charged-reckless', 'https://runrepeat.com/inov-8-terraclaw-250', 'https://runrepeat.com/reebok-sublite-xt-cushion-2-0', 'https://runrepeat.com/hoka-one-one-constant', 'https://runrepeat.com/adidas-solar-rnr', 'https://runrepeat.com/asics-gel-fujirunnegade', 'https://runrepeat.com/puma-mobium-elite-v2', 'https://runrepeat.com/saucony-fastwitch-8', 'https://runrepeat.com/nike-air-zoom-odyssey-2', 'https://runrepeat.com/asics-endurant', 'https://runrepeat.com/asics-gt-2000-5', 'https://runrepeat.com/la-sportiva-bushido', 'https://runrepeat.com/under-armour-thrill-2', 'https://runrepeat.com/salomon-sense-propulse', 'https://runrepeat.com/asics-gel-scram-3', 'https://runrepeat.com/new-balance-1540', 'https://runrepeat.com/adidas-pure-boost-x', 'https://runrepeat.com/inov-8-rocklite-286-gtx', 'https://runrepeat.com/nike-free-rn-distance-2', 'https://runrepeat.com/asics-gel-excite-4', 'https://runrepeat.com/asics-gel-equation', 'https://runrepeat.com/newton-distance-s', 'https://runrepeat.com/new-balance-vazee-pace-v2', 'https://runrepeat.com/mizuno-wave-catalyst-2', 'https://runrepeat.com/asics-33-fa', 'https://runrepeat.com/armour-micro-g-speed-swift', 'https://runrepeat.com/asics-gel-zaraca', 'https://runrepeat.com/nike-air-max-2017', 'https://runrepeat.com/adidas-kanadia-8', 'https://runrepeat.com/inov-8-x-talon-225', 'https://runrepeat.com/new-balance-910-v3', 'https://runrepeat.com/salomon-sonic-aero', 'https://runrepeat.com/asics-gel-ds-trainer-22', 'https://runrepeat.com/asics-gel-kahana-8', 'https://runrepeat.com/saucony-nomad-tr', 'https://runrepeat.com/altra-impulse', 'https://runrepeat.com/puma-propel', 'https://runrepeat.com/under-armour-spine-disrupt', 'https://runrepeat.com/adidas-duramo-8', 'https://runrepeat.com/adidas-kanadia-gtx', 'https://runrepeat.com/armour-speedform-slingride', 'https://runrepeat.com/under-armour-drift', 'https://runrepeat.com/new-balance-fresh-foam-boracay-v3', 'https://runrepeat.com/new-balance-770', 'https://runrepeat.com/salomon-s-lab-speed', 'https://runrepeat.com/altra-lone-peak-3-0-neoshell-mid', 'https://runrepeat.com/brooks-hyperion', 'https://runrepeat.com/saucony-kinvara-8', 'https://runrepeat.com/asics-gel-cumulus-18-gtx', 'https://runrepeat.com/la-sportiva-ultra-raptor-gtx', 'https://runrepeat.com/saucony-redeemer', 'https://runrepeat.com/nike-air-zoom-streak-lt', 'https://runrepeat.com/nike-air-max-tailwind', 'https://runrepeat.com/altra-lone-peak-30-neoshell-low', 'https://runrepeat.com/asics-gel-cumulus-19', 'https://runrepeat.com/asics-gt-1000-6', 'https://runrepeat.com/skechers-gomeb-razor', 'https://runrepeat.com/nike-free-rn-motion-flyknit-2017', 'https://runrepeat.com/salomon-sense-mantra', 'https://runrepeat.com/saucony-excursion-tr-10', 'https://runrepeat.com/inov-8-roclite-290', 'https://runrepeat.com/mizuno-wave-prophecy-6', 'https://runrepeat.com/salomon-s-lab-xa-alpine', 'https://runrepeat.com/mizuno-wave-sayonara-4', 'https://runrepeat.com/nike-zoom-fly', 'https://runrepeat.com/asics-fuzex-lyte', 'https://runrepeat.com/adidas-terrex-agravic-gtx', 'https://runrepeat.com/puma-ignite-ultimate', 'https://runrepeat.com/adidas-galaxy-trail', 'https://runrepeat.com/inov-8-roadclaw-275', 'https://runrepeat.com/puma-ignite-proknit', 'https://runrepeat.com/puma-speed-300-ignite', 'https://runrepeat.com/nike-air-zoom-terra-kiger-4']
#'https://runrepeat.com/puma-voltage-disc',
print(len(urlList))
writer = csv.writer(csv_file)
writer.writerow(['Company','ShoeURL','ShoeName','colorSize','TotalScore','TotalReviews','Discontinued','Terrain','Arch','Use','Price','Discount','ShoeWeight',
                 'ToeDrop','FootHeight','ReleaseDate','GoodSummary','BadSummary','Summary','RatingsText','USARanking',
                 'FiveStars','FourStars','ThreeStars','TwoStars','OneStars','ProdInfo','SizenFit','OuterSole','UpperSole'])
#urlList = "https://runrepeat.com/brooks-ghost-10".split(",")
for shoeURL in urlList:
    print(shoeURL)
    driver.get(shoeURL)
    time.sleep(3)
    totalScore = driver.find_elements_by_xpath('.//div[@class="runscore-value"]')[0].text
    totalReviews = driver.find_elements_by_xpath('//div[@class="stars-container"]/div/a')[0].text 
    companyName = driver.find_elements_by_xpath('//div[@class="aggregate_rating_wrapper"]/a/img')[0].get_attribute("alt")
    shoeName = driver.find_elements_by_xpath('.//h1[@class="p-name main-shoe-title"]/span')[0].text
    
    try:
        colorCount =  len(driver.find_elements_by_xpath('//*[@class="color_images col-xs-12"]/div'))
    except Exception as e:
        colorCount = 0

    #get facts
    #check if discontinued
    try:
        itemFound =  driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_discontinued"]/div/div[2]/div[1]/div')[0].text
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
        actualPrice = 0
    try:
        #if there is discounted price
        discountPrice = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_price"]/div/div[2]/div[1]/div/a')[0].text
    except Exception as e:
        discountPrice = 0
    #check if there is a release date
    try:
        releaseDate = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_release-date"]/div/div[2]/div[1]/div')[1].text
    except Exception as e:
        releaseDate = ""
    try:
        USARanking = driver.find_elements_by_xpath('//*[@class="rr_section_content rr_compare_content popular_section_continents_map"]/div/p')[0].text
    except Exception as e:
        USARanking = ""
    
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

    try:
        prodInfo=""
        txtList =  driver.find_elements_by_xpath('//*[@class="product-updates"]/ul/li')
        for txt in txtList:
            prodInfo += txt.text +";"
    except Exception as e:
        prodInfo = ""
    try:
        sizenFit =  driver.find_elements_by_xpath('//*[@class="size-and-fit"]/p')[1].text
    except Exception as e:
        sizenFit = ""
    try:
        outSole =  driver.find_elements_by_xpath('//*[@class="outsole"]/p')[1].text
    except Exception as e:
        outSole = ""        
    try:
        upperS =  driver.find_elements_by_xpath('//*[@class="upper"]/p')[1].text
    except Exception as e:
        upperS = ""
        
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
        driver.execute_script("window.scrollTo(0,1000)")
        clickButton[0].click()
        time.sleep(2)
        shoeWeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_weight"]/div/div[2]/div[1]/div[2]/div[2]')[0].text
        heelToeDrop = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_heel-to-toe-drop"]/div/div[2]/div[1]/div[2]/div')[1].text
        foreFootHeight = driver.find_elements_by_xpath('//*[@class="col-md-12 col-xs-12 fact-item fact-item_forefoot-height"]/div/div[2]/div[1]/div[2]/div')[1].text
    except Exception as e:
        shoeWeight = ""
        heelToeDrop = ""
        foreFootHeight = ""
    #assign values to dictionary
    runningShoeDict['Company'] = companyName
    runningShoeDict['URL'] = shoeURL
    runningShoeDict['ShoeName'] = shoeName
    runningShoeDict['ShoeColors'] = colorCount
    runningShoeDict['TotalScore'] = totalScore
    runningShoeDict['TotalReviews'] = totalReviews
    runningShoeDict['Discontinued'] = discontinuedShoe
    runningShoeDict['Terrain'] = bestTerrain
    runningShoeDict['Arch'] = archSupport
    runningShoeDict['Use'] = bestUse
    runningShoeDict['Price'] = actualPrice
    runningShoeDict['Discount'] = discountPrice
    runningShoeDict['ShoeWeight'] = shoeWeight
    runningShoeDict['ToeDrop'] = heelToeDrop
    runningShoeDict['FootHeight'] = foreFootHeight
    runningShoeDict['ReleaseDate'] = releaseDate
    runningShoeDict['GoodSummary'] = goodSummaryStr
    runningShoeDict['BadSummary'] = badSummaryStr
    runningShoeDict['Summary'] = aggSummaryStr
    runningShoeDict['RatingsText'] = ratingsText
    runningShoeDict['USARanking'] = USARanking
    runningShoeDict['FiveStars'] = fiveStars
    runningShoeDict['FourStars'] = fourStars
    runningShoeDict['ThreeStars'] = threeStars
    runningShoeDict['TwoStars'] = twoStars
    runningShoeDict['OneStars'] = oneStars
    
    runningShoeDict['ProdInfo'] = prodInfo
    runningShoeDict['SizenFit'] = sizenFit
    runningShoeDict['OuterSole'] = outSole
    runningShoeDict['UpperSole'] = upperS
    
    try:
        writer.writerow(runningShoeDict.values())
    except Exception as e:
        continue
#end of for loop
csv_file.close()
driver.close()