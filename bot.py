import os

import discord
from dotenv import load_dotenv


def connect_bot():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(token)


def soup():
    return True


if __name__ == '__main__':
    connect_bot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
