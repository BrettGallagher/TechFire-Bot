import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import asyncio
import time

from profanity import profanity

Client = discord.Client()
client = commands.Bot(command_prefix="^")
custom_badwords = ["douche", "bitch", "asshole", "ass", "swerve"] #makes custom profanity filter triggers
profanity.load_words(custom_badwords)
@client.event
async def on_ready(): #initialization
    print(client.user.name)
    print("is Setup!")
    await client.change_presence(game=discord.Game(name="Getting ready for the 2019 season!", type=3))

def remove_formatting(text):
    return ''.join([x.lower() for x in text if ord(x) != 42 and ord(x) != 95 and ord(x) != 126 and ord(x) != 96]) #makes all forms of text able to be understood by bot

@client.event
async def on_message(message):
        if remove_formatting(message.content) == "what events are we going to?":
            await client.send_message(message.channel, "We are going to Springside Chestnut Hill and Montgomery!")
        elif remove_formatting(message.content) == "We are going to Springside Chestnut Hill and Montgomery!":
            await client.send_message(message.channel, "We are going to Springside Chestnut Hill and Montgomery!")


@client.event #profanity filter
async def on_message(message):

    if profanity.contains_profanity(message.content):
        await client.delete_message(message)
        await client.send_message(message.channel, "That is not GP!")
        print("Bad word removed")













client.run("Don't steal my Token please")
