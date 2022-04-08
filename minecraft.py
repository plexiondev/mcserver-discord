# import
from mcstatus import JavaServer
import discord
from discord.ext import commands
import datetime
import asyncio
import json
# custom colours in terminal
from colorama import init
from colorama import Fore, Back, Style
init()

try:
    file = open("config.json","r")
    json = json.loads(file.read())
except FileNotFoundError:
    print (f"{Back.RED}{Style.BRIGHT}[ERROR]{Style.RESET_ALL} Missing 'config.json' file, see documentation.")
    exit()

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
    print (f"{Back.GREEN}{Style.BRIGHT}[READY]{Style.RESET_ALL} Signed in as {bot.user}")
    
    global message
    channel = bot.get_channel(text_channel)
    message = await channel.fetch_message(message_id)
    
    while True:
        current_date = datetime.datetime.now()
        current_time = current_date.strftime("%H:%M:%S")
        try:
            print (f"{Back.GREEN}{Style.BRIGHT}[SENT]{Style.RESET_ALL}  Updated at {Style.BRIGHT}{current_time}{Style.RESET_ALL}   {Fore.GREEN}({server_ip} in <#{text_channel}>){Style.RESET_ALL}")
            # lookup
            server = JavaServer.lookup(server_ip)
            
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
                await bot.change_presence(activity=discord.Game(f"with {status.players.online} players"))
            else:
                embed = discord.Embed(
                    title = server_name,
                    description = f"{online_message}{status.description}",
                    colour = 0x7581ef
                )
                embed.add_field(name = "Online", value = f"0/{player_limit}", inline = True)
                await bot.change_presence(activity=discord.Game(f"with nobody online.."))
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
            await bot.change_presence(activity=discord.Game(f"offline!"))
            await message.edit(embed = embed)

        await asyncio.sleep(3)

bot.run(token)
