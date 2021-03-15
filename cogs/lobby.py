import discord
import requests
import json
from discord.ext import commands

class Lobby(commands.Cog):

  def __init__(self, client):
    self.client = client

  def get_quote(self):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " \n-" + json_data[0]['a']
    return(quote)

  @commands.command()
  async def hello(self, ctx):
    await ctx.send(f"Hello **{ctx.author.mention}**, I am **{ctx.message.guild.name}** server's assistant bot with codename **{self.client.user.mention}** designed by MuffinCrunchy. My priority is to help each member's needs, so you can call me anytime. I am currently still in the development stage and will continue to develop, if you have any criticism and suggestions please contact my master.")

  @commands.command()
  async def inspire(self, ctx):
    quote = self.get_quote()
    await ctx.send(quote)

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f"Your status now is {round(self.client.latency * 1000)}ms")

  @commands.command()
  # async def clear(self, ctx):
  async def clear(self, ctx, limit: int=None):
    count = 0
    async for msg in ctx.message.channel.history(limit=limit):
      count += 1
    await ctx.channel.purge(limit=count)
    await(await ctx.send(f'Cleared by {ctx.author.mention}')).delete(delay=4)
    await ctx.message.delete()

def setup(client):
  client.add_cog(Lobby(client))