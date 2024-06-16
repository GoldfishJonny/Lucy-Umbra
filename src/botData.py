from discord import *
from os import *
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient

dotenv_path = Path('../.env')

def getIntents():
    intents = Intents.default()
    intents.message_content = True

    return intents

def getClient():
    return Client(intents=getIntents())

def getTree():
    return app_commands.CommandTree(getClient())

def getToken():
    load_dotenv(dotenv_path=dotenv_path)
    return getenv("TOKEN")

def getCommandBot():
    return commands.Bot(command_prefix=".",intents=getIntents())

def get_database():
    load_dotenv(dotenv_path=dotenv_path)
    client = MongoClient(getenv("DATABASE"))
    return client['Lucy']

def runClient(client):
    client.run(getToken())