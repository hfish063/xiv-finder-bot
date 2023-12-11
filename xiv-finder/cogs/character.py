import discord
from discord.ext import commands
import requests

"""
Cog containing character related commands
author: haydenfish
"""

class Character(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Character(bot))