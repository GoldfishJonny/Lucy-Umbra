from discord import *
from discord.http import *
from botData import *
import save

bot = getCommandBot()
botguilds = bot.guilds
guild = Object(id=1053783383475495012)

@bot.tree.command(name="setuplogger", description="Setup logging", guild=guild)
async def setuplogger(interaction:Interaction, arg:TextChannel):
    await interaction.response.send_message(f"Will add logger into channel")
#Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync(guild=guild)
    print(f"Works!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    save.createDoc(guild)
    print(f"lmao")


bot.run(getToken())