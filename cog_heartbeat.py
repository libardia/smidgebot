from discord.ext import tasks
from discord.ext.commands import Cog
import config
import logger

class Heartbeat(Cog):
    def __init__(self):
        self.num_heartbeats = 0

    @Cog.listener()
    async def on_ready(self):
        self.heartbeat.start()

    @tasks.loop(hours=1)
    async def heartbeat(self):
        self.num_heartbeats += 1
        await logger.log(f'Bot is alive. {self.num_heartbeats} heartbeats since last restart.')

def setup(bot):
    bot.add_cog(Heartbeat())
