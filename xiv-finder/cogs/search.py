import discord
from discord.ext import commands
import requests

"""
Cog containing item search related commands
author: haydenfish

TODO: Command descriptions, embed creation method, fix missing argument bug
"""

RESULT_LIMIT = 5

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # ffxiv api url, do not change
        self.url = "https://xivapi.com"

    """
    Generalized method for search command, takes category type and object name as parameters, returns embed message list containing 
    related data obtained from api requests
    Search algorithm uses post wildcard matching, e.g. test*
    """
    @commands.command()
    async def search(self, ctx, category, *name):
        # important: convert name tuple into string
        name_str = ' '.join(name)

        results = self.request_result_list(category, name_str)

        for index, item in enumerate(results[:RESULT_LIMIT]):
            embed = discord.Embed(title = item['Name'], color = discord.Color.dark_gray())

            embed.set_image(url = self.find_icon(item['Icon']))
            embed.set_footer(text = f'Result: {index}')

            await ctx.send(embed = embed)

    """
    Searches for single object from user provided category, returns embed object containing related data
    obtained from ffxivapi requests
    Search algorithm uses exact matching
    """
    @commands.command()
    async def match(self, ctx, category, *name):
        # important: convert name tuple into string
        name_str = ' '.join(name)

        result = self.request_match_result(category, name_str)

        # TODO: move to request method
        if len(result) < 1:
            raise Exception("Unable to locate object with name - " + name_str)

        # important: item data contained in first element of result list
        item = result[0]

        embed = discord.Embed(title = item['Name'], color = discord.Color.dark_blue())

        embed.set_image(url = self.find_icon(item['Icon']))
        embed.set_footer(text = 'Matching query result')
            
        await ctx.send(embed = embed)


    def request_result_list(self, category, name):
        search_url = self.url + "/search"

        response = requests.get(search_url, params = {'indexes': category, 'string': name})

        load_response = response.json()

        return load_response['Results']
    
    def request_match_result(self, category, name):
        search_url = self.url + "/search"

        response = requests.get(search_url, params = {'indexes': category, 'string': name, 'string_algo': 'match'})

        if response.status_code != 200:
            raise Exception("Request failed - invalid http status code: check endpoint")

        load_response = response.json()

        return load_response['Results']
    
    def find_icon(self, name):
        return self.url + name


async def setup(bot):
    await bot.add_cog(Search(bot))