import discord
from discord.ext import commands
import requests

RESULT_LIMIT = 5
URL = "https://xivapi.com"

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("successful")

    """
    Sends list of embed objects containing name, description, and icon image of specific item
    Search algorithm uses post wildcard matching, e.g. test*
    """
    @commands.command()
    async def items(self, ctx, *args):
        results, status = self.request_result_list(args)

        for index, result in enumerate(results[:RESULT_LIMIT]):
            embed = discord.Embed(title = result['Name'], color = discord.Color.dark_gray())

            if status == 200:
                embed.set_image(url = self.find_icon(result['Icon']))
                embed.add_field(name = "Description", value = self.request_description(result['Url']))


            await ctx.send(embed = embed)

    """
    Sends a single embed object containing name, description, and icon image of specific item
    Search algorithm uses exact matching
    If item with corresponding name is not found, notify user
    """
    @commands.command()
    async def item(self, ctx, *args):
        return

    def request_result_list(self, name):
        search_url = URL + "/search"

        response = requests.get(search_url, params = {'indexes': 'Item', 'string': name})
        load_response = response.json()

        return load_response['Results'], response.status_code
    
    def request_description(self, id):
        search_url = URL + str(id)

        response = requests.get(search_url).json()

        load_response = response['BaseParam0']
        
        # if there is no description available
        if load_response == None:
            return "Description unavailable"
        
        return load_response['Description']
    
    def find_icon(self, name):
        return URL + name


async def setup(bot):
    await bot.add_cog(search(bot))