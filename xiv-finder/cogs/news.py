import discord
from discord.ext import commands
from datetime import datetime
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
    Sends list of embed messages containing data relating to this months news topics to user,
    length of list is defined by optional command arg, default value is 10
    """
    @commands.command()
    async def topics(self, ctx, result_limit = 10):
        topic_list = self.request_topic_list()

        for topic in topic_list[:int(result_limit)]:
            if self.is_same_month(topic):
                await ctx.send(embed = self.create_news_embed(topic))
    
    def request_topic_list(self):
        search_url = URL + "/topics"

        response = requests.get(search_url)

        load_response = response.json()

        return load_response
    
    def create_news_embed(self, topic):
        if topic is None:
            return 

        news = discord.Embed(title = topic['title'], url = topic['url'], color = discord.Color.red())

        news.add_field(name = 'Description', value = topic['description'])
        news.set_image(url = topic['image'])
        news.set_footer(text = topic['time'])

        return news
    
    def is_same_month(self, topic):
        current_month = datetime.now().strftime('%m').replace('0', '')

        topic_month = str(topic['time']).split('-')[1]

        return current_month == topic_month

async def setup(bot):
    await bot.add_cog(News(bot))