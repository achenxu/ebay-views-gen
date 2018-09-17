import discord
from discord.ext import commands
import requests
from random import randint
import random
import time


requests.packages.urllib3.disable_warnings()

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
   
    if message.content.startswith('!ebayviews'):
        old = message.content
        url = old.replace("!ebayviews", "").strip()
        print ("Viewer started")

        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }

        for i in range(50):
            try:
                r =  requests.get(url,headers=headers1,verify=False,timeout=5)
                if r.status_code == 200:
                    print ("Viewed successfully")
                
            except Exception as e:
                print(e)
        
        embed = discord.Embed(title="", color=0x00ff00)
        embed.add_field(name="Item finished being viewed 50 times", value="made by thebotsmith#0001", inline=True)
        await client.send_message(message.channel, embed=embed)


    if message.content == ('!help'):
        embed = discord.Embed(title="", color=0x00ff00)
        embed.add_field(name="Give 50 views to an item", value="!ebayviews url", inline=True)

        await client.send_message(message.channel, embed=embed)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

while True:
    client.run(TOKEN)
