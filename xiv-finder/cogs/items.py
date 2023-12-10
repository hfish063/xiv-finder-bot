import discord
from discord.ext import commands
import requests

"""
Cog containing item search related commands
author: haydenfish

TODO: Documentation, util method to validate http status code from ffxivapi requests
"""

RESULT_LIMIT = 5
URL = "https://xivapi.com"

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("successful")

    """
    Sends list of embed messages containing name, description, and icon image of specific item
    Search algorithm uses post wildcard matching, e.g. test*
    """
    @commands.command()
    async def items(self, ctx, *args):
        results, status = self.request_result_list(args)

        if status != 200:
            return

        for index, item in enumerate(results[:RESULT_LIMIT]):
            embed = discord.Embed(title = item['Name'], color = discord.Color.dark_gray())

            embed.set_image(url = self.find_icon(item['Icon']))
            embed.add_field(
                name = "Description", 
                value = self.request_description(item['Url']))

            await ctx.send(embed = embed)

    """
    Sends a single embed message containing name, description, and icon image of specific item
    Search algorithm uses exact matching
    If item with corresponding name is not found, notify user
    """
    @commands.command()
    async def item(self, ctx, *args):
        # placeholder item name
        result, status = self.request_match_item("sword of ascension")

        if status != 200:
            return

        item = result[0]

        # debugging comment
        # await ctx.send(str(result))

        embed = discord.Embed(title = item['Name'], color = discord.Color.dark_blue())

        embed.set_image(url = self.find_icon(item['Icon']))
        embed.add_field(
            name = "Description",
            value = self.request_description(item['Url']))
            
        await ctx.send(embed = embed)

    def request_result_list(self, name):
        search_url = URL + "/search"

        response = requests.get(search_url, params = {'indexes': 'Item', 'string': name})
        load_response = response.json()

        return load_response['Results'], response.status_code
    
    def request_match_item(self, name):
        search_url = URL + "/search"

        response = requests.get(search_url, params = {'indexes': 'Item', 'string': name, 'string_algo': 'match'})
        load_response = response.json()

        return load_response['Results'], response.status_code
    
    def request_description(self, id):
        search_url = URL + str(id)

        response = requests.get(search_url).json()

        load_response = response['BaseParam0']
        
        # placeholder if there is no description available
        if load_response == None:
            return "Description unavailable"
        
        return load_response['Description']
    
    def find_icon(self, name):
        return URL + name


async def setup(bot):
    await bot.add_cog(search(bot))