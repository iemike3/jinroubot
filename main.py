
import discord,json,datetime
from discord.ext import commands

class helpcommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "へるぷ"

    def get_ending_note(self):
        return ("Github:https://github.com/iemike3/jinroubot")

bot = commands.Bot(command_prefix="j.",help_command=helpcommand())

with open("config.json","r") as f:
    config = json.load(f)

@bot.event
async def on_ready():
    print("---------------------")
    print(f"User:{bot.user}")
    print(f"Login Time:{datetime.datetime.now()}")
    print("---------------------")

class WereWolf_Main(commands.Cog,name="人狼コマンド"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def start(self,ctx):
        await ctx.send("start command run")

    @commands.command()
    async def stop(self,ctx):
        await ctx.send("stop command end")

bot.add_cog(WereWolf_Main(bot=bot))
bot.run(config["token"])
