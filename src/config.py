import os
from configparser import ConfigParser

_CONFIG_PATH = os.path.join(os.getcwd(), 'smidgebot.ini')
configs: ConfigParser = None

TOKEN_INSTRUCTIONS = '<copy your token here>'

SECTION_BOT = 'Bot'
VALUE_TOKEN = 'Token'
VALUE_DATAPATH = 'DataPath'

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
    
    with open(_CONFIG_PATH, 'w') as cfile:
        configs.write(cfile)

def token():
    return configs.get(SECTION_BOT, VALUE_TOKEN)

def dataPath():
    return configs.get(SECTION_BOT, VALUE_DATAPATH)
