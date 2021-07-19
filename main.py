import discord
import os
import random
import json
from discord.ext import commands
from settings import *

bot = commands.Bot(command_prefix='!')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('{0.user} is here to steal your heart!'.format(bot))


bot.run(DISCORD_BOT_TOKEN)