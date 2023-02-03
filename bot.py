import os

import discord
from dotenv import load_dotenv

from bs4 import BeautifulSoup
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def connect_bot():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(token)


def extract_html(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--headless")
    chrome_driver = os.getcwd() + "\\chromedriver.exe"
    s = Service(chrome_driver)
    driver = webdriver.Chrome(options=chrome_options, service=s)
    driver.get(url)
    driver.implicitly_wait(220)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
    driver.implicitly_wait(120)
    time.sleep(3)
    result = driver.page_source
    soup = BeautifulSoup(result, 'html.parser')
    return soup


def parse_html(soup):
    listings = soup.ol.extract()
    num_count = int(listings.find("div").string[0])
    # line finds div attribute that shows how many results there are.
    # craigslist gives recommended listings as well, but I only want actual listings
    all_listings = listings.find_all("li")[0:num_count]
    for listing in all_listings:
        print(listing)





if __name__ == '__main__':
    link = "https://slo.craigslist.org/search/san-luis-obispo-ca/apa?availabilityMode=2&housing_type=10&housing_type=11&housing_type=12&housing_type=2&housing_type=3&housing_type=4&housing_type=5&housing_type=6&housing_type=7&housing_type=8&housing_type=9&lat=35.2958&lon=-120.6606&min_bedrooms=3&search_distance=1.4#search=1~list~0~0"
    html = extract_html(link)
    parse_html(html)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
