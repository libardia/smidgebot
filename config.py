import os
from configparser import ConfigParser

# Some constants to be used elsewhere
_CONFIG_PATH = os.path.join(os.getcwd(), 'smidgebot.ini')
TOKEN_INSTRUCTIONS = '<copy your token here>'

SECTION_BOT = 'Bot'
VALUE_TOKEN = 'Token'
VALUE_DATAPATH = 'DataPath'
VALUE_LOGPATH = 'LogPath'
VALUE_PREFIX = 'Prefix'
SECTION_SETTINGS = 'Settings'
VALUE_LOGCHANNEL_ENABLED = 'LogChannelEnabled'
VALUE_LOGCHANNEL_ID = 'LogChannelId'
VALUE_LOGCHANNEL_RETAIN_SECONDS = 'LogChannelRetainSeconds'

# The configs
configs: ConfigParser = None

# This should be called in smidgebot.py before the bot starts
def init(base_path):
    global configs
    configs = ConfigParser()
    configs.optionxform = str
    if os.path.exists(_CONFIG_PATH):
        configs.read(_CONFIG_PATH)

    if SECTION_BOT not in configs:
        configs[SECTION_BOT] = {}
    bot = configs[SECTION_BOT]
    if VALUE_TOKEN not in bot:
        bot[VALUE_TOKEN] = TOKEN_INSTRUCTIONS
    if VALUE_DATAPATH not in bot:
        bot[VALUE_DATAPATH] = os.path.join(base_path, 'smidgebot.data')
    if VALUE_LOGPATH not in bot:
        bot[VALUE_LOGPATH] = os.path.join(base_path, 'smidgebot.log')
    if VALUE_PREFIX not in bot:
        bot[VALUE_PREFIX] = '!'

    if SECTION_SETTINGS not in configs:
        configs[SECTION_SETTINGS] = {}
    settings = configs[SECTION_SETTINGS]
    if VALUE_LOGCHANNEL_ENABLED not in settings:
        settings[VALUE_LOGCHANNEL_ENABLED] = 'false'
    if VALUE_LOGCHANNEL_ID not in settings:
        settings[VALUE_LOGCHANNEL_ID] = ''
    if VALUE_LOGCHANNEL_RETAIN_SECONDS not in settings:
        # Default is 1 week
        settings[VALUE_LOGCHANNEL_RETAIN_SECONDS] = str(7 * 24 * 60 * 60)
    
    with open(_CONFIG_PATH, 'w') as cfile:
        configs.write(cfile)

# Convenience getters
def getToken():
    return configs.get(SECTION_BOT, VALUE_TOKEN)

def getDataPath():
    return configs.get(SECTION_BOT, VALUE_DATAPATH)

def getLogPath():
    return configs.get(SECTION_BOT, VALUE_LOGPATH)

def getPrefix():
    return configs.get(SECTION_BOT, VALUE_PREFIX)

def getLogChannelEnabled():
    return configs.getboolean(SECTION_SETTINGS, VALUE_LOGCHANNEL_ENABLED)

def getLogChannelId():
    return configs.getint(SECTION_SETTINGS, VALUE_LOGCHANNEL_ID)

def getLogChannelRetainSeconds():
    return configs.getint(SECTION_SETTINGS, VALUE_LOGCHANNEL_RETAIN_SECONDS)
