import config
import util
from datetime import datetime
from discord.ext.commands import Bot
from discord.channel import TextChannel

_logfile = None
_logchannel: TextChannel = None

def init(bot: Bot):
    global _logfile
    global _logchannel
    _logfile = config.getLogPath()
    if config.getLogChannelEnabled():
        _logchannel = bot.get_channel(config.getLogChannelId())

async def log(msg):
    msg = f'[{datetime.now().astimezone()}] {msg}'
    print(msg)
    with open(_logfile, 'a') as f:
        f.write(msg + '\n')
    if _logchannel:
        await _logchannel.send(f'```{util.etb(msg)}```')
