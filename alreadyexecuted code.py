# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:18:53 2017

@author: Lalith Mambalam
"""

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
    
    
    
    for linkURL in linksLists:
    try:
        print("scraping shoe page " + str(linkURL))
        #
        #driver.get(linkURL)
    except Exception as e:
        print(e)
        driver.close
        break
    
    ['https://runrepeat.com/brooks-ghost-10', 'https://runrepeat.com/adidas-ultra-boost-uncaged',
     'https://runrepeat.com/new-balance-860-v7', 'https://runrepeat.com/adidas-adistar-boost-esm', 
     'https://runrepeat.com/adidas-tracerocker', 'https://runrepeat.com/adidas-ultra-boost-x', 'https://runrepeat.com/salomon-speedcross-4-cs', 'https://runrepeat.com/puma-ignite-evoknit', 'https://runrepeat.com/adidas-adizero-boston-boost', 'https://runrepeat.com/on-cloudflow', 'https://runrepeat.com/salomon-kalalau', 'https://runrepeat.com/nike-air-zoom-pegasus-34', 'https://runrepeat.com/nike-flyknit-racer', 'https://runrepeat.com/brooks-cascadia-12', 'https://runrepeat.com/brooks-revel', 'https://runrepeat.com/mizuno-wave-rider-20', 'https://runrepeat.com/adidas-terrex-swift-r-gtx', 'https://runrepeat.com/brooks-caldera', 'https://runrepeat.com/asics-33-m', 'https://runrepeat.com/asics-gel-noosa-tri-11', 'https://runrepeat.com/skechers-flex-appeal-2-0', 'https://runrepeat.com/asics-dynaflyte', 'https://runrepeat.com/adidas-vigor-6-tr', 'https://runrepeat.com/asics-gel-sendai', 'https://runrepeat.com/nike-air-zoom-vomero-12', 'https://runrepeat.com/merrell-bare-access-arc', 'https://runrepeat.com/merrell-crush-light', 'https://runrepeat.com/on-cloud', 'https://runrepeat.com/new-balance-990-v4', 'https://runrepeat.com/adidas-pureboost-xpose', 'https://runrepeat.com/merrell-all-out-crush', 'https://runrepeat.com/brooks-launch-4', 'https://runrepeat.com/inov-8-mudclaw-300', 'https://runrepeat.com/asics-gel-kayano-24', 'https://runrepeat.com/on-cloudsurfer', 'https://runrepeat.com/new-balance-vazee-rush-v2', 'https://runrepeat.com/asics-gel-kinsei', 'https://runrepeat.com/brooks-purecadence-6', 'https://runrepeat.com/on-cloudflyer', 'https://runrepeat.com/under-armour-speedform-apollo', 'https://runrepeat.com/hoka-one-one-tor-ultra-hi-wp', 'https://runrepeat.com/adidas-ultra-boost', 'https://runrepeat.com/brooks-glycerin-15', 'https://runrepeat.com/altra-escalante', 'https://runrepeat.com/adidas-response-boost', 'https://runrepeat.com/new-balance-840', 'https://runrepeat.com/adidas-terrex-agravic-speed', 'https://runrepeat.com/brooks-adrenaline-gts-17', 'https://runrepeat.com/nike-lunarstelos', 'https://runrepeat.com/puma-carson-runner', 'https://runrepeat.com/asics-gel-quantum-180-2', 'https://runrepeat.com/nike-fs-lite-run-4', 'https://runrepeat.com/new-balance-vazee-prism-v2', 'https://runrepeat.com/adidas-ultra-boost-st', 'https://runrepeat.com/armour-speedform-fortis-vent', 'https://runrepeat.com/mizuno-wave-inspire-13', 'https://runrepeat.com/adidas-supernova', 'https://runrepeat.com/under-armour-dash-rn-2', 'https://runrepeat.com/skechers-gorun-5', 'https://runrepeat.com/asics-gel-venture-6', 'https://runrepeat.com/nike-air-zoom-elite-9', 'https://runrepeat.com/brooks-pureflow-6', 'https://runrepeat.com/la-sportiva-mutant', 'https://runrepeat.com/salomon-speedcross-4-gtx', 'https://runrepeat.com/inov-8-x-talon-212', 'https://runrepeat.com/saucony-shadow-6000', 'https://runrepeat.com/brooks-transcend-4', 'https://runrepeat.com/saucony-breakthru', 'https://runrepeat.com/asics-gel-evate', 'https://runrepeat.com/salomon-speedcross-4', 'https://runrepeat.com/puma-tazon-6-mesh', 'https://runrepeat.com/armour-micro-g-assert-6', 'https://runrepeat.com/nike-flex-fury-2', 'https://runrepeat.com/asics-gel-contend-4', 'https://runrepeat.com/puma-ignite', 'https://runrepeat.com/adidas-alphabounce-engineered-mesh', 'https://runrepeat.com/nike-lunarepic-flyknit', 'https://runrepeat.com/asics-gel-quantum-360', 'https://runrepeat.com/saucony-ride-10', 'https://runrepeat.com/hoka-one-one-valor', 'https://runrepeat.com/new-balance-610', 'https://runrepeat.com/adidas-powerblaze', 'https://runrepeat.com/adidas-element-refine-tricot', 'https://runrepeat.com/puma-ignite-disc', 'https://runrepeat.com/nike-lunarepic-low-flyknit-2', 'https://runrepeat.com/salomon-sonic-pro', 'https://runrepeat.com/salomon-x-scream-foil', 'https://runrepeat.com/nike-free-rn', 'https://runrepeat.com/nike-air-zoom-winflo-4', 'https://runrepeat.com/adidas-adizero-takumi-sen', 'https://runrepeat.com/inov-8-x-talon-200', 'https://runrepeat.com/salomon-x-mission-3', 'https://runrepeat.com/adidas-alphabounce', 'https://runrepeat.com/nike-downshifter-7', 'https://runrepeat.com/brooks-addiction', 'https://runrepeat.com/saucony-echelon', 'https://runrepeat.com/hoka-one-one-arahi', 'https://runrepeat.com/saucony-peregrine-7', 'https://runrepeat.com/armour-charged-bandit-2', 'https://runrepeat.com/new-balance-1210-v3', 'https://runrepeat.com/hoka-one-one-gaviota', 'https://runrepeat.com/asics-gel-foundation', 'https://runrepeat.com/nike-lunartempo', 'https://runrepeat.com/asics-patriot-8', 'https://runrepeat.com/merrell-all-out-crush-tough-mudder', 'https://runrepeat.com/merrell-pace-glove', 'https://runrepeat.com/saucony-xodus-iso-runshield', 'https://runrepeat.com/salomon-xa-pro-3d-gtx', 'https://runrepeat.com/nike-flex-experience-rn-6', 'https://runrepeat.com/salomon-speedcross-vario', 'https://runrepeat.com/saucony-freedom-iso', 'https://runrepeat.com/merrell-all-out-charge', 'https://runrepeat.com/inov-8-roclite-282-gtx', 'https://runrepeat.com/adidas-terrex-x-king', 'https://runrepeat.com/skechers-gorun-400', 'https://runrepeat.com/saucony-omni-15', 'https://runrepeat.com/nike-free-rn-flyknit-2017', 'https://runrepeat.com/adidas-terrex-agravic', 'https://runrepeat.com/nike-zoom-all-out-low', 'https://runrepeat.com/brooks-puregrit-6', 'https://runrepeat.com/asics-gel-surveyor-5', 'https://runrepeat.com/nike-air-max-sequent-2', 'https://runrepeat.com/adidas-terrex-skychaser', 'https://runrepeat.com/puma-ignite-mesh', 'https://runrepeat.com/saucony-lancer', 'https://runrepeat.com/merrell-all-out-peak', 'https://runrepeat.com/saucony-cohesion-10', 'https://runrepeat.com/adidas-vengeful', 'https://runrepeat.com/adidas-energy-cloud', 'https://runrepeat.com/inov-8-terraclaw-220', 'https://runrepeat.com/hoka-one-one-bondi-5', 'https://runrepeat.com/nike-lunar-skyelux', 'https://runrepeat.com/newton-distance-elite', 'https://runrepeat.com/adidas-terrex-fast-r-gtx', 'https://runrepeat.com/vibram-fivefingers-kso-evo', 'https://runrepeat.com/armour-fat-tire-gtx', 'https://runrepeat.com/adidas-energy-boost', 'https://runrepeat.com/saucony-kineta-relay', 'https://runrepeat.com/adidas-alphabounce-ams', 'https://runrepeat.com/asics-gel-sonoma-3', 'https://runrepeat.com/newton-motion', 'https://runrepeat.com/nike-air-zoom-span', 'https://runrepeat.com/hoka-one-one-clifton-4', 'https://runrepeat.com/asics-gel-exalt', 'https://runrepeat.com/la-sportiva-akasha', 'https://runrepeat.com/nike-lunarglide-9', 'https://runrepeat.com/adidas-adizero-adios-boost', 'https://runrepeat.com/salomon-x-scream-3d', 'https://runrepeat.com/armour-speedform-slingshot', 'https://runrepeat.com/hoka-one-one-valor-ltr', 'https://runrepeat.com/adidas-duramo-lite', 'https://runrepeat.com/vibram-fivefingers-v-run', 'https://runrepeat.com/puma-ignite-pwrwarm', 'https://runrepeat.com/inov-8-roclite-305', 'https://runrepeat.com/vibram-fivefingers-kmd-sport', 'https://runrepeat.com/merrell-vapor-glove', 'https://runrepeat.com/adidas-mana-bounce-2', 'https://runrepeat.com/new-balance-fresh-foam-zante-v3', 'https://runrepeat.com/mizuno-synchro-mx', 'https://runrepeat.com/la-sportiva-ultra-raptor', 'https://runrepeat.com/vibram-fivefingers-spyridon-mr', 'https://runrepeat.com/salomon-speedcross-pro', 'https://runrepeat.com/nike-air-zoom-structure-20', 'https://runrepeat.com/inov-8-x-claw-275', 'https://runrepeat.com/salomon-xa-pro-3d-cs-wp', 'https://runrepeat.com/new-balance-880-v7', 'https://runrepeat.com/la-sportiva-wildcat-gtx', 'https://runrepeat.com/armour-charged-reckless', 'https://runrepeat.com/inov-8-terraclaw-250', 'https://runrepeat.com/reebok-sublite-xt-cushion-2-0', 'https://runrepeat.com/hoka-one-one-constant', 'https://runrepeat.com/adidas-solar-rnr', 'https://runrepeat.com/asics-gel-fujirunnegade', 'https://runrepeat.com/puma-mobium-elite-v2', 'https://runrepeat.com/saucony-fastwitch-8', 'https://runrepeat.com/nike-air-zoom-odyssey-2', 'https://runrepeat.com/asics-endurant', 'https://runrepeat.com/asics-gt-2000-5', 'https://runrepeat.com/la-sportiva-bushido', 'https://runrepeat.com/under-armour-thrill-2', 'https://runrepeat.com/salomon-sense-propulse', 'https://runrepeat.com/asics-gel-scram-3', 'https://runrepeat.com/new-balance-1540', 'https://runrepeat.com/adidas-pure-boost-x', 'https://runrepeat.com/inov-8-rocklite-286-gtx', 'https://runrepeat.com/nike-free-rn-distance-2', 'https://runrepeat.com/asics-gel-excite-4', 'https://runrepeat.com/asics-gel-equation', 'https://runrepeat.com/newton-distance-s', 'https://runrepeat.com/new-balance-vazee-pace-v2', 'https://runrepeat.com/mizuno-wave-catalyst-2', 'https://runrepeat.com/asics-33-fa', 'https://runrepeat.com/armour-micro-g-speed-swift', 'https://runrepeat.com/asics-gel-zaraca', 'https://runrepeat.com/nike-air-max-2017', 'https://runrepeat.com/adidas-kanadia-8', 'https://runrepeat.com/inov-8-x-talon-225', 'https://runrepeat.com/new-balance-910-v3', 'https://runrepeat.com/salomon-sonic-aero', 'https://runrepeat.com/asics-gel-ds-trainer-22', 'https://runrepeat.com/asics-gel-kahana-8', 'https://runrepeat.com/saucony-nomad-tr', 'https://runrepeat.com/altra-impulse', 'https://runrepeat.com/puma-propel', 'https://runrepeat.com/under-armour-spine-disrupt', 'https://runrepeat.com/adidas-duramo-8', 'https://runrepeat.com/adidas-kanadia-gtx', 'https://runrepeat.com/armour-speedform-slingride', 'https://runrepeat.com/under-armour-drift', 'https://runrepeat.com/new-balance-fresh-foam-boracay-v3', 'https://runrepeat.com/new-balance-770', 'https://runrepeat.com/salomon-s-lab-speed', 'https://runrepeat.com/altra-lone-peak-3-0-neoshell-mid', 'https://runrepeat.com/brooks-hyperion', 'https://runrepeat.com/saucony-kinvara-8', 'https://runrepeat.com/asics-gel-cumulus-18-gtx', 'https://runrepeat.com/la-sportiva-ultra-raptor-gtx', 'https://runrepeat.com/saucony-redeemer', 'https://runrepeat.com/nike-air-zoom-streak-lt', 'https://runrepeat.com/nike-air-max-tailwind', 'https://runrepeat.com/altra-lone-peak-30-neoshell-low', 'https://runrepeat.com/asics-gel-cumulus-19', 'https://runrepeat.com/asics-gt-1000-6', 'https://runrepeat.com/skechers-gomeb-razor', 'https://runrepeat.com/nike-free-rn-motion-flyknit-2017', 'https://runrepeat.com/salomon-sense-mantra', 'https://runrepeat.com/saucony-excursion-tr-10', 'https://runrepeat.com/inov-8-roclite-290', 'https://runrepeat.com/mizuno-wave-prophecy-6', 'https://runrepeat.com/salomon-s-lab-xa-alpine', 'https://runrepeat.com/mizuno-wave-sayonara-4', 'https://runrepeat.com/nike-zoom-fly', 'https://runrepeat.com/asics-fuzex-lyte', 'https://runrepeat.com/adidas-terrex-agravic-gtx', 'https://runrepeat.com/puma-ignite-ultimate', 'https://runrepeat.com/adidas-galaxy-trail', 'https://runrepeat.com/inov-8-roadclaw-275', 'https://runrepeat.com/puma-ignite-proknit', 'https://runrepeat.com/puma-speed-300-ignite', 'https://runrepeat.com/nike-air-zoom-terra-kiger-4']