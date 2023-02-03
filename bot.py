import os

import discord
from dotenv import load_dotenv

import urllib.request
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


def connect_bot():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(token)


def craig_soup(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--headless")
    chrome_driver = os.getcwd() + "\\chromedriver.exe"
    s = Service(chrome_driver)
    print(chrome_driver)
    driver = webdriver.Chrome(options=chrome_options, service=s)

    driver.get(url)
    html_text = driver.page_source
    print(html_text)



if __name__ == '__main__':
    link = "https://slo.craigslist.org/search/san-luis-obispo-ca/apa?availabilityMode=2&housing_type=10&housing_type=11&housing_type=12&housing_type=2&housing_type=3&housing_type=4&housing_type=5&housing_type=6&housing_type=7&housing_type=8&housing_type=9&lat=35.2922&lon=-120.6576&min_bedrooms=3&search_distance=1.38#search=1~list~0~0"
    craig_soup(link)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
