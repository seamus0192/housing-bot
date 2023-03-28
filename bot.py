import os

import discord
from dotenv import load_dotenv
from scrape import *
from datetime import date

    
def main(link,link2):
    currtime = date.today()
    if 5 <= currtime.month <= 9:
        print("out of season")
        return 0
    
    #looks for .env file where token is stored privately
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    
    #channel where message is sent to
    channel = 1070420022427664396

    client = discord.Client(intents=intents)

    # Once client is ready, sends a message to the console and begins to extract html/ listings
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        craigslist_html = extract_html(link)
        await parse_craigslist(craigslist_html, client, channel)
        apartments_html = extract_html(link2)
        print(apartments_html.prettify())
        await client.close()

    client.run(token, reconnect=False)


if __name__ == '__main__':
    #craigslist search query to be parsed
    search = "https://slo.craigslist.org/search/san-luis-obispo-ca/apa?availabilityMode=2&housing_type=10" \
             "&housing_type=11&housing_type=12&housing_type=2&housing_type=3&housing_type=4&housing_type=5" \
             "&housing_type=6&housing_type=7&housing_type=8&housing_type=9&lat=35.2958&lon=-120.6606&min_bedrooms=3" \
             "&search_distance=1.4#search=1~list~0~0"
    search2 = "https://www.apartments.com/houses-townhomes/min-3-bedrooms/?sk=1ee49f3b127682cf038898a69fc3f23d&bb=jjx158-36Nj_0l1G"
    main(search, search2)
