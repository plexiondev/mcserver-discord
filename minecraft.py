# import
from mcstatus import MinecraftServer
import discord
from discord.ext import commands
import datetime
import asyncio
import json

file = open("config.json","r")
json = json.loads(file.read())

token = json["token"]
server_ip = json["server_ip"]
server_formal_ip = json["server_formal_ip"]
server_name = json["server_name"]
player_limit = json["player_limit"]
ignore_no_query = json["ignore_no_query"]
online_message = json["online_message"]
offline_message = json["offline_message"]

text_channel = json["channel"]
message_id = json["message_id"]

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    global message
    print ("\nready!\n")
    channel = bot.get_channel(text_channel)
    message = await channel.fetch_message(message_id)
    
    while True:
        current_date = datetime.datetime.now()
        current_time = current_date.strftime("%H:%M:%S")
        try:
            print (f"updated: {current_time}")
            # lookup
            server = MinecraftServer.lookup(server_ip)
            
            # get current status
            status = server.status()
            # players
            query_enabled = 0
            try:
                query = server.query()
                query_enabled = 1
            except:
                query_enabled = 0
            
            # player count
            if status.players.online >= 1:
                embed = discord.Embed(
                    title = server_name,
                    description = f"{online_message}{status.description}",
                    colour = 0x76f755
                )
                embed.add_field(name = "Online", value = f"{status.players.online}/50", inline = True)
            else:
                embed = discord.Embed(
                    title = server_name,
                    description = f"{online_message}{status.description}",
                    colour = 0x7581ef
                )
                embed.add_field(name = "Online", value = f"0/{player_limit}", inline = True)
            # player list
            # empty lists return False
            if query_enabled == 1:
                if query.players.names:
                    embed.add_field(name = "Players", value = f"{', '.join(query.players.names)}", inline = True)
                else:
                    embed.add_field(name = "Players", value = "Nobody online", inline = True)
            elif ignore_no_query != "true":
                embed.add_field(name = "Players", value = "`enable_query` is disabled server-side.", inline = True)
            embed.add_field(name = "Connect", value = server_formal_ip, inline = True)
            embed.set_footer(text = f"Last updated {current_time}")
            await message.edit(embed = embed)
        except:
            embed = discord.Embed(
                title = server_name,
                description = offline_message,
                colour = 0xed5956
            )
            embed.set_footer(text = f"Last updated {current_time}")
            await message.edit(embed = embed)

        await asyncio.sleep(3)

bot.run(token)
