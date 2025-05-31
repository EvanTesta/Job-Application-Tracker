from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def read_url(urlString):
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--headless=new")
    chrome_Service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service = chrome_Service, options=options)
    driver.get(urlString)
    time.sleep(5)
    title = driver.title
    driver.quit()
    print(title)
    return title


def read_url_ziprecruiter(urlString):
    driver = webdriver.Chrome("C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver.get(urlString)
    print(driver.title)
    driver.quit()