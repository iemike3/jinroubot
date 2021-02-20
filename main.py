
import discord,json,datetime
from discord.ext import commands

bot = commands.Bot(command_prefix="j_")

with open("config.json","r") as f:
    config = json.load(f)

@bot.event
async def on_ready():
    print("---------------------")
    print(f"User:{bot.user}")
    print(f"Login Time:{datetime.datetime.now()}")

bot.run(config["token"])
