import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="^")


@client.event
async def on_ready():
    print(client.user.name)
    print("is Setup!")
    await client.change_presence(game = discord.Game(name = "Getting ready for the 2019 season!"))

def remove_formatting(text):
    return ''.join([x.lower() for x in text if ord(x) != 42 and ord(x) != 95 and ord(x) != 126 and ord(x) != 96]) #makes all forms of text able to be understood by bot

@client.event
async def on_message(message):

        if remove_formatting(message.content) == "what events are we going to?":
            await client.send_message(message.channel, "We are going to Springside Chestnut Hill and Montgomery!")
        elif remove_formatting(message.content) == "We are going to Springside Chestnut Hill and Montgomery!":
            await client.send_message(message.channel, "We are going to Springside Chestnut Hill and Montgomery!")
















client.run("NTA2MTc0NzE1NTE0MDYwODMw.DsU0qw.aOSiDA-C8KIWMDlgydJ74QzQhd8")
