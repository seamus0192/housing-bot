from bs4 import BeautifulSoup
import pandas as pd
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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


async def parse_html(soup, client):
    listings = soup.ol.extract()
    num_count = int(listings.find("div").string[0])
    # line finds div attribute that shows how many results there are.
    # craigslist gives recommended listings as well, but I only want actual listings
    old_df = pd.read_csv(os.getcwd() + "/listings.csv")['Title'].tolist()
    print(old_df)
    all_listings = listings.find_all("li")[0:num_count]
    listing_info = {'Title': [], 'Link': [], 'Price': [], 'Bedrooms': []}
    for listing in all_listings:
        e1 = listing.find('a').text
        e2 = listing.find('a')['href']
        e3 = listing.find(class_="priceinfo").text
        e4 = listing.find(class_="housing-meta").text
        listing_info['Title'].append(e1)
        listing_info['Link'].append(e2)
        listing_info['Price'].append(e3)
        listing_info['Bedrooms'].append(e4)
        if e1 not in old_df:
            print(f"entered for {e1}")
            channel = client.get_channel(1070420022427664396)
            await channel.send(format_message(e1, e2, e3, e4))
    df = pd.DataFrame(listing_info)
    df.to_csv(os.getcwd() + "/listings.csv")


def format_message(e1, e2, e3, e4):
    return f"A new property has been listed! \n {e1} \n Price: {e3} Size: {e4} \n Link: {e2}"
