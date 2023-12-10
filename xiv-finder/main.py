import discord
from discord.ext import commands

"""
main module for Findxiv bot

Documentation can be found here: [github]
"""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', activity = discord.Game(name = "Type !help for list of commands"), intents=intents)

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"{guild.id}: {guild.name}")

        guild_count = guild_count + 1

    print("Findxiv bot is in " + str(guild_count) + " guilds")

    await bot.load_extension("cogs.items")

if __name__ == "__main__":
    bot.run("MTE4Mjc5ODcxMDY4MjQyNzQ2Mw.G10A4S.WBaJVQCacFlqrtauHEvdEpDbZoROQGRZGjywXo")
