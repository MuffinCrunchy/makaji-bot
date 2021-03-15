import discord
import datetime
from discord.ext import commands, tasks
from itertools import cycle

class Status(commands.Cog):

  def __init__(self, client):
    self.client = client

  stats = cycle(["Genshin Impact", "Minecraft", "Cyberpunk 2077", "Civilization VI", "UNO", "Hollow Knight", "My Time at Portia", "Counter Strike: Global Offensive", "Valorant", "League of Legends", "Rise of the Tomb Raider"])

  @commands.Cog.listener()
  async def on_ready(self):
    self.change_status.start()
    print(f"Bot have logged in as {self.client.user}")
    # Test Channel: 787231881233825792
    # Main Channel: 804379375700410368
    await self.client.get_channel(804379375700410368).send(embed=embed)

  @tasks.loop(seconds=7200)
  async def change_status(self):
    await self.client.change_presence(activity=discord.Game(next(self.stats)))
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send("Sorry, I don't have a command like that.")

  @commands.Cog.listener()
  async def on_member_join(self, member):
    embed = discord.Embed(title="Welcome to our civilization", description="Your permission has been granted by Our Supreme Leader", color=0xA997DF)
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="User ID: ", value=member.id)
    embed.add_field(name="User Name: ", value=member.display_name)
    embed.add_field(name="Server Name: ", value=member.guild)
    embed.add_field(name="User Serial: ", value=len(list(member.guild.members)))
    embed.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"))
    embed.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"))

    # Test Channel: 787231881233825792
    # Main Channel: 804379375700410368
    await self.client.get_channel(804379375700410368).send(embed=embed)


  @commands.Cog.listener()
  async def on_member_remove(self, member):
    embed = discord.Embed(title="May God always be with you", description="Your existence has been erased by Our Supreme Leader", color=0xA997DF)
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="User ID: ", value=member.id)
    embed.add_field(name="User Name: ", value=member.display_name)
    embed.add_field(name="Server Name: ", value=member.guild)
    embed.add_field(name="User Serial: ", value=len(list(member.guild.members)))
    embed.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"))
    embed.add_field(name="Left at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"))

    # Test Channel: 787231881233825792
    # Main Channel: 804379375700410368
    await self.client.get_channel(804379375700410368).send(embed=embed)

def setup(client):
  client.add_cog(Status(client))