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
import datetime
from Ticket import TicketQuery
import re

# driver = webdriver.Safari()
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# Get website content
driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")


def stations():
    # Stations list (later this data os going to be taken from website)
    station_list = ['Adana', 'Adapazarı', 'Adatepe (Pingen)', 'Adnanmenderes Havaalanı', 'Afyon A.Çetinkaya',
                    'Ahmetler',
                    'Akhisar', 'Aksakal', 'Akçadağ', 'Akçamağara', 'Alifuatpaşa', 'Alöve', 'Ankara Gar', 'Araplı',
                    'Arifiye',
                    'Arıkören', 'Atça', 'Avşar', 'Aydın', 'Ayran', 'Ayrancı', 'Ayvacık', 'Aşkale', 'Bahçe',
                    'Bahçeli (Km.755+290 S)', 'Bahçeşehir', 'Bakır', 'Balışıh', 'Banaz', 'Bandırma Şehir', 'Baskil',
                    'Batman',
                    'Battalgazi', 'Bağıştaş', 'Bedirli', 'Belemedik', 'Bereket', 'Beyhan', 'Beylikköprü', 'Beylikova',
                    'Beyoğlu',
                    'Beşiri', 'Bilecik', 'Bismil', 'Biçer', 'Bor', 'Bostankaya', 'Bozkurt', 'Bozüyük',
                    'Boğazköprü Müselles',
                    'Buharkent', 'Böğecik', 'Büyükderbent YHT', 'Caferli', 'Ceyhan', 'Cürek', 'Demirdağ', 'Demirkapı',
                    'Demiryurt',
                    'Denizli', 'Doğançay', 'Doğanşehir', 'Durak', 'Ekerek', 'Elazığ', 'Elmadağ', 'Emiralem', 'Erbaş',
                    'Ereğli',
                    'Ergani', 'Eriç', 'Erzurum', 'Eskişehir', 'Eşme', 'Fırat', 'Gaziemir', 'Gebze', 'Germencik',
                    'Gezin',
                    'Goncalı', 'Goncalı Müselles', 'Gölbaşı Gar', 'Gölcük', 'Gömeç', 'Göçentaşı', 'Güllübağ', 'Gümüş',
                    'Güneş',
                    'Gürpınar', 'Hacıkırı', 'Hacırahmanlı', 'Hanlı', 'Hasankale', 'Hekimhan', 'Himmetdede', 'Horozköy',
                    'Horozluhan', 'Horsunlu', 'Huzurkent', 'Hüyük', 'Ildızım', 'Ilıca', 'Irmak', 'Kadılı', 'Kalecik',
                    'Kalkancık',
                    'Kandilli', 'Kanlıca', 'Kapaklı', 'Kapıdere İstasyonu', 'Karaali', 'Karaali', 'Karaağaçlı',
                    'Karabük',
                    'Karaisalıbucağı', 'Karaköy', 'Karalar', 'Karaman', 'Karaosman', 'Karasenir', 'Karasu', 'Karaurgan',
                    'Karaözü', 'Kars', 'Kavaklıdere', 'Kayseri', 'Kayışlar', 'Kaşınhan', 'Kelebek', 'Kemah',
                    'Kemaliye Çaltı',
                    'Kemerhisar', 'Kiremithane (adana)', 'Km.139+500', 'Km.156 Durak', 'Km.171+000', 'Km.176+000',
                    'Km.186+000',
                    'Km.282+200', 'Km.286+500', 'Km.638+907', 'Km.746+840', 'Konaklar', 'Konya', 'Kozdere',
                    'Kumlu Sayding',
                    'Kurbağalı', 'Kurt', 'Kurtalan', 'Kuyucak', 'Kuşcenneti', 'Kuşsarayı', 'Köprüağzı', 'Köprüköy',
                    'Köşk', 'Kürk',
                    'Kılıçlar', 'Kırkağaç', 'Kırıkkale', 'Lalahan', 'Leylek', 'Maden', 'Malatya', 'Mamure', 'Manisa',
                    'Menderes',
                    'Menemen', 'Mithatpaşa', 'Muradiye', 'Muş', 'Narlı Gar', 'Nazilli', 'Niğde', 'Nurdağ', 'Ortaklar',
                    'Osmancık',
                    'Osmaneli', 'Osmaniye', 'Oturak', 'Palandöken', 'Palu', 'Pamukören', 'Pancar', 'Paşalı', 'Polatlı',
                    'Polatlı YHT', 'Pozantı', 'Pınarlı', 'Rahova', 'Salat', 'Salihli', 'Sallar', 'Sapanca', 'Sarayköy',
                    'Saruhanlı', 'Sarıdemir', 'Sarıkamış', 'Sarıkent', 'Sarımsaklı', 'Savaştepe', 'Sağlık', 'Selçuk',
                    'Sevindik',
                    'Sincan', 'Sivas', 'Sivrice', 'Soğucak', 'Sudurağı', 'Susurluk', 'Suveren', 'Suçatı', 'Söke',
                    'Söğütlü Durak',
                    'Süngütaşı', 'Sünnetçiler', 'Tanyeri', 'Tatvan Gar', 'Taşkent', 'Tecer', 'Tepeköy', 'Topaç',
                    'Topdağı',
                    'Toprakkale', 'Torbalı', 'Tuzhisar', 'Tüney', 'Türkoğlu', 'Ulam', 'Ulukışla', 'Uluova', 'Umurlu',
                    'Urganlı',
                    'Uşak', 'Vezirhan', 'Yahşihan', 'Yahşiler', 'Yakapınar', 'Yarbaşı', 'Yayla', 'Yaylıca', 'Yazlak',
                    'Yenifakılı',
                    'Yenikangal', 'Yeniköy', 'Yeniçubuk', 'Yerköy', 'Yeşilhisar', 'Yolçatı', 'Yunusemre', 'Yurt',
                    'Çakmak',
                    'Çalıköy', 'Çankırı', 'Çavundur', 'Çağlar', 'Çerikli', 'Çerkeş', 'Çetinkaya', 'Çiğli', 'Çobanhasan',
                    'Çukurhüseyin', 'Çumra', 'Çöltepe', 'İnay', 'İncesu(Kayseri)', 'İncirlik', 'İncirliova', 'İsabeyli',
                    'İshakçelebi', 'İsmetpaşa', 'İstanbul(Pendik)', 'İzmir (Basmane)', 'Şakirpaşa', 'Şarkışla',
                    'Şefaatli',
                    'Şefkat', 'Şehitlik']
    return station_list


def is_ticket_available(ticket_query):
    for date in [ticket_query.start_date + datetime.timedelta(days=i) for i in
                 range(int((ticket_query.end_date - ticket_query.start_date).days))]:
        # Fill "from" box
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nereden")))
        search = driver.find_element(By.ID, "nereden")
        search.send_keys(ticket_query.fro)

        # Fill "to" box
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nereye")))
        search = driver.find_element(By.ID, "nereye")
        search.send_keys(ticket_query.to)

        # Set the date
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "trCalGid_input")))
        search = driver.find_element(By.ID, "trCalGid_input")
        search.clear()
        date_editted = ".".join[date.day, date.month, date.year]
        search.send_keys(date_editted)

        # find and click button even if there is another object in front of it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Ara')]")))
        search_button = driver.find_element(By.XPATH, "//span[contains(text(),'Ara')]")
        driver.execute_script("arguments[0].click();", search_button)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody[@id='mainTabView:gidisSeferTablosu_data']")))
        table = driver.find_element(By.XPATH, "//tbody[@id='mainTabView:gidisSeferTablosu_data']")
        text = table.text.strip()

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
            train_matrix.append(
                list(filter(None, trains[i].split("\n"))))  # remove empty strings "" by using filter method
        train_matrix = list(filter(None, train_matrix))  # remove empty lists []

        print(train_matrix)
        ticket_list = []
        for train in train_matrix:
            if re.match(r"\d+ Aktarma", train[3]):  # if it is an indirect travel
                train_number = train[3].split()[0]

            else:
                train_number = 1
                ticket_list.append(
                    ticket_query("Ankara Gar", "Balıkesir", train[0], train[1], train[3], train[4], int(train[-1][2:-3]),
                                 int(train[-2][-2])))

        for ticket_query in ticket_list:
            print(ticket_query.start_date)
