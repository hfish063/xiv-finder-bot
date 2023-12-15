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
        topic_list = self.request_news_list('topic')

        # TODO: additional verification
        if int(result_limit) < 1:
            result_limit = 1

        for topic in topic_list[:int(result_limit)]:
            if self.is_same_month(topic):
                await ctx.send(embed = self.create_news_embed(topic))

    """
    Sends list of embed messages containing data relating to this months maintenance (server downtime) events
    """
    @commands.command()
    async def maintenance(self, ctx):
        maint_list = self.request_news_list('maintenance')

        for result in maint_list:
            if self.is_same_month(result):
                await ctx.reply(embed = self.create_maintenance_embed(result))
    
    def request_news_list(self, type):
        search_url = self.create_request_url(type)

        response = requests.get(search_url)

        load_response = response.json()

        return load_response
    
    # TODO: do we really need both of these request methods?
    # def request_maintenance_list(self):
    #     search_url = URL + "/maintenance"

    #     response = requests.get(search_url)

    #     load_response = response.json()

    #     return load_response
    
    """
    Return string containing api search url for specified query type
    """
    def create_request_url(self, type: str):
        if type == 'topic':
            return URL + "/topics"
        elif type == 'maintenance':
            return URL + "/maintenance"

    def create_news_embed(self, topic):
        if topic is None:
            return 

        news = discord.Embed(title = topic['title'], url = topic['url'], color = discord.Color.red())

        news.add_field(name = 'Description', value = topic['description'])
        news.set_image(url = topic['image'])
        news.set_footer(text = topic['time'])

        return news
    
    def create_maintenance_embed(self, result):
        if result is None:
            return
        
        maintenance = discord.Embed(title = result['title'], url = result['url'], color = discord.Color.orange())

        maintenance.add_field(name = 'Start: ', value = result['start'])
        maintenance.add_field(name = 'End: ', value = result['end'])
        maintenance.set_footer(text = result['id'])

        return maintenance
    
    def is_same_month(self, topic):
        current_month = datetime.now().strftime('%m').replace('0', '')

        topic_month = str(topic['time']).split('-')[1]

        return current_month == topic_month

async def setup(bot):
    await bot.add_cog(News(bot))