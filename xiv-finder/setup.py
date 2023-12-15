import discord
import os
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

"""
main module for Findxiv bot

Documentation can be found here: [github]
"""

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', activity = discord.Game(name = "Type !help for list of commands"), intents = intents)

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"{guild.id}: {guild.name}")

        guild_count = guild_count + 1

    print("Findxiv bot is in " + str(guild_count) + " guilds")

    await bot.load_extension("cogs.search")
    await bot.load_extension("cogs.news")

    # stub until class implementation is complete
    # await bot.load_extension("cogs.character")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Not a valid command, type !help for list of available commands")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Missing required argument(s), type !help for more details")
    else:
        raise error

"""
Ping command for debugging usage
TODO: expected removal
"""
@commands.command()
async def ping(self, ctx):
    await ctx.send("successful")

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
