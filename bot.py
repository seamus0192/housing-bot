import os

import discord
from dotenv import load_dotenv
from scrape import *

def main(link):
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
        html = extract_html(link)
        await parse_html(html, client, channel)
        await client.close()

    client.run(token)


if __name__ == '__main__':
    #craigslist search query to be parsed
    search = "https://slo.craigslist.org/search/san-luis-obispo-ca/apa?availabilityMode=2&housing_type=10" \
             "&housing_type=11&housing_type=12&housing_type=2&housing_type=3&housing_type=4&housing_type=5" \
             "&housing_type=6&housing_type=7&housing_type=8&housing_type=9&lat=35.2958&lon=-120.6606&min_bedrooms=3" \
             "&search_distance=1.4#search=1~list~0~0"
    main(search)
