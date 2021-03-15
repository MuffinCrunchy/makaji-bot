import discord
from discord.ext import commands

class VoiceConnect(commands.Cog):

  def __init__(self, client):
    self.client = client

  # @commands.command()
  # async def join(self, ctx):
  #   global voice
  #   channel = ctx.message.author.voice.channel
  #   voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

  #   if voice and voice.is_connected():
  #     await voice.move_to(channel)
  #   else:
  #     voice = await channel.connect()

  #   await voice.disconnect()

  #   if voice and voice.is_connected():
  #     await voice.move_to(channel)
  #   else:
  #     voice = await channel.connect()
    
  #   await ctx.send(f"Joined {channel}")

  # @commands.command()
  # async def leave(self, ctx):
  #   await ctx.voice_client.disconnect()


def setup(client):
  client.add_cog(VoiceConnect(client))