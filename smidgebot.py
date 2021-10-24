from os import path
import config
import logger
from discord.ext import commands
import discord.errors

# Initialize modules and bot
config.init(path.dirname(path.abspath(__file__)))
bot = commands.Bot(command_prefix=config.getPrefix())
bot.load_extension('cog_heartbeat')

@bot.event
async def on_ready():
    logger.init(bot)
    await logger.log(f'BOT STARTED. We have logged in as "{bot.user}"')
    await logger.log(f'Command prefix is "{config.getPrefix()}".')

try:
    bot.run(config.getToken())
except discord.errors.LoginFailure:
    print(f'Failed to log in; is the token correct? It\'s set as: {config.getToken()}')
