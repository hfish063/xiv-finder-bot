import discord
from discord.ext import commands
import requests

"""
Cog containing character related commands
author: haydenfish
"""

URL = ""

class Character(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def character(self, ctx, name, server):
        return
    
    def request_character(self, name, server):
        return

async def setup(bot):
    await bot.add_cog(Character(bot))