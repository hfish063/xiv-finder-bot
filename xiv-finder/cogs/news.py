import discord
from discord.ext import commands
import requests

"""
Cog containing news related commands
author: haydenfish
"""

# lodestone api url, do not change
URL = "https://na.lodestonenews.com/news"

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    Sends list of this months news topics to user
    """
    @commands.command()
    async def topics(self, ctx):
        topic_list = self.request_topic_list()

        for topic in topic_list:
            await ctx.send(topic['title'])
    
    def request_topic_list(self):
        search_url = URL + "/topics"

        response = requests.get(search_url)

        load_response = response.json()

        return load_response
    
    # TODO: return embed object containing topic related data
    def news_embed(self):
        return
    
    # TODO: create method to verify topic is from the current month
    def verify_time(self):
        return

async def setup(bot):
    await bot.add_cog(News(bot))