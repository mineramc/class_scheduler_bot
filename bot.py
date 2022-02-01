# bot.py
import os

import discord
import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='echo', help="Responds to the command's invoker")
async def echo(ctx):
    current_time = datetime.datetime.now()
    await ctx.send("Testing commands. " + str(current_time))

print(TOKEN)
bot.run(TOKEN)