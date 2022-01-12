# import
import discord
from discord.ext import commands
import json

file = open("config.json","r")
json = json.loads(file.read())

token = json["token"]

text_channel = json["channel"]

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    global message
    print ("\nmessage sent!\nyou can now close this window and follow the readme instructions.\n")
    channel = bot.get_channel(text_channel)
    
    embed = discord.Embed(
        title = "Placeholder",
        description = "no need to worry",
        colour = 0x76f755
    )
    await channel.send(embed = embed)


bot.run(token)