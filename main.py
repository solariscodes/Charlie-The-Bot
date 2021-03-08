'''
Simple Discord bot written in Python
It returns a random Chuck Norris's phrase when someone gets online
by Solriscodes
07/03/2021
'''
import discord
import os
import json
import requests

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def Norris():
  api = "https://api.chucknorris.io/jokes/random"
  req = requests.get(api)
  c1 = json.loads(req.text)
  return c1['value']

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

class Bot():
  @client.event
  async def on_ready():
      print("Starting {0.user}".format(client))
  @client.event
  async def on_message(message):    
      if message.author == client.user:
        return
      if message.content.startswith('entrou'):
        await message.channel.send("Hello back!")
  @client.event
  async def on_member_update(before, after):
    await before.send(Norris())            
  client.run(os.getenv('TOKEN'))    
Bot()