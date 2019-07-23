import discord
from discord.ext import commands
import json
import asyncio
import time
from profanity import profanity
import aiotba
import datetime
from random import *
current = datetime.datetime.now()
Client = discord.Client()
client = commands.Bot(command_prefix="^")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gpquote = sample(number, 1)
if number > [5]:
    gpquote = "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence"
elif number < [5]:
    gpquote = "ok"


@client.event
async def on_ready():
    print(client.user.name)
    print("is Setup!")
    await client.change_presence(game=discord.Game(name="Preparing for IRI!", type=3))

@client.event
async def on_message():
    global gpquote
    #number = random.randint(1, 10)
    #if number == 1:
       # gpquote = "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence"


@client.event
async def on_message(message):

    if profanity.contains_profanity(message.content):
        await client.delete_message(message)
        await client.send_message(message.channel, gpquote)

@client.event
async def on_message_delete(message):
    deldoc = open("deleted messages.txt", "a",)
    await deldoc.write(message.content + ";" + str(current) +"|")




client.run("Place Token Here")
