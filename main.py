
import discord,json
from discord.ext import commands

bot = commands.Bot(command_prefix="j_")

with open("config.json","r") as f:
    config = json.load(f)

bot.run(config["token"])
