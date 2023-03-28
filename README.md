# SLO-Housing-Bot

The main purpose of this bot is to track rental listing in the neighborhood around Cal Poly SLO. It is generally very difficult for students to find houses, as the market is very competitive, so having listings notified pretty immediately after they are listed could help those who are frustrated with housing.

This program runs once an hour, opening Craigslist and using crontab to send new messages to discord. Over the half of the season the bot was active this year (late jan 2023 - apr 2023), it recorded over 100 listings!

Uses pandas (csv editing), sellinium (driver, allows for scaping with a dynamically loaded website such as github), and discord.py (as a method of sending updates to a group of people) as tools to build a script that when ran, identifies new listings (relative to the last time the script was ran locally) and sends them on discord.
