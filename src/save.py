from discord import *
from botData import *

def createDoc(guild):
    db = get_database()
    entry = {
        "guild": guild.id
    }
    db["guilds"].insert_one(entry)