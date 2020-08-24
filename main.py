from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
from time import sleep


#login to NationStates
with open("credentials") as file:
    nation, password, target = file.read().split(",")
    driver = webdriver.Firefox()
    driver.get("https://www.nationstates.net/page=login")
    driver.find_element_by_xpath("/html/body/div[3]/div/form/fieldset/table/tbody/tr[1]/td[2]/input").send_keys(nation)
    driver.find_element_by_xpath("/html/body/div[3]/div/form/fieldset/table/tbody/tr[2]/td[2]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[3]/div/form/fieldset/table/tbody/tr[4]/td[2]/p/button").click()
    sleep(2)
        
    #Initiating combat loop
    while True:
        #Go to challenge against designated ennemy 
        driver.get("https://www.nationstates.net/page=challenge?entity_name=" + target)
        driver.find_element_by_xpath("/html/body/div[3]/div/form/p[2]/input").click()
        sleep(1)
 
        #Combat management
        roundString = "trumps-clicker-round-1"
        if ("You won!" in driver.page_source):
            while True:
                print(roundString)
                try:
                    driver.find_element_by_id(roundString).click()
                    sleep(5)
                except:
                    break
                roundString = roundString[:-1] + chr(ord(roundString[-1]) + 1)
            sleep(1)