import os
from configparser import ConfigParser

# Some constants to be used elsewhere
_CONFIG_PATH = os.path.join(os.getcwd(), 'smidgebot.ini')
TOKEN_INSTRUCTIONS = '<copy your token here>'

SECTION_BOT = 'Bot'
VALUE_TOKEN = 'Token'
VALUE_DATAPATH = 'DataPath'
VALUE_PREFIX = 'Prefix'

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
        bot[VALUE_DATAPATH] = os.path.join(base_path, 'data.p')
    if VALUE_PREFIX not in bot:
        bot[VALUE_PREFIX] = '!'
    
    with open(_CONFIG_PATH, 'w') as cfile:
        configs.write(cfile)

# Convenience getters
def getToken():
    return configs.get(SECTION_BOT, VALUE_TOKEN)

def getDataPath():
    return configs.get(SECTION_BOT, VALUE_DATAPATH)

def getPrefix():
    return configs.get(SECTION_BOT, VALUE_PREFIX)
