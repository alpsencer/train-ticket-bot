import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re

# SPATH = "/usr/bin/safaridriver
# FPATH = "/Users/alpsencer/Desktop/SeleniumDrivers/geckodriver"
# os.environ['PATH'] += "/Users/alpsencer/Desktop/SeleniumDrivers/"
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#driver = webdriver.Safari()
# Get website content
driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nereden")))
# Fill "from" box
search = driver.find_element(By.ID, "nereden")
search.send_keys("Ankara Gar")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nereye")))
# Fill "to" box
search = driver.find_element(By.ID, "nereye")
search.send_keys("Balıkesir")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "trCalGid_input")))
# Set the date
search = driver.find_element(By.ID, "trCalGid_input")
search.clear()
search.send_keys("07.07.2022")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Ara')]")))
# find and click button even if there is another object in front of it
searchButton = driver.find_element(By.XPATH, "//span[contains(text(),'Ara')]")
driver.execute_script("arguments[0].click();", searchButton)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody[@id='mainTabView:gidisSeferTablosu_data']")))

table = driver.find_element(By.XPATH, "//tbody[@id='mainTabView:gidisSeferTablosu_data']")

trainList = table.text.split("seç")
for i in trainList:
    print(re.findall("(\d+)", i))
print(trainList)


