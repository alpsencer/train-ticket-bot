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
from Ticket import Ticket

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
text = table.text.strip()

print(table.text)
""" (Example text)
07.07.2022
09:30
8s:22dk
1 Aktarma 07.07.2022
17:52
i
YHT : ANKARA-İSTANBUL : ( Ankara Gar - Eskişehir ) 09.30 - 10.56
Standart
Esnek
i
ANAHAT : EGE EKSPRESİ : ( Eskişehir - Balıkesir ) 12.10 - 17.52
Standart
Esnek
2+2 Pulman (Ekonomi) (9)

2+1 Pulman (1. Mevki) (1)

₺ 158,00
Seç

07.07.2022
21:00
8s:39dk
08.07.2022
05:39
i
ANAHAT : İZMİR MAVİ
Standart
Esnek
2+1 Pulman (1. Mevki) (0)

₺ 121,00
Seç
"""

trains = table.text.split("Seç")
train_matrix = []


for i in range(len(trains)):
    train_matrix.append(list(filter(None, trains[i].split("\n"))))  # remove empty strings "" by using filter method
train_matrix = list(filter(None, train_matrix))  # remove empty lists []

print(train_matrix)
ticket_list = []
for train in train_matrix:
    if re.match("[0-9] Aktarma", train[3]):  # if it is an indirect travel
        pass
    else:
        ticket_list.append(Ticket("Ankara Gar", "Balıkesir", train[0], train[1], train[3], train[4], int(train[-1][2:-3]), int(train[-2][-2])))


for ticket in ticket_list:
    print(ticket.start_date)