import discord
from discord.ext import commands

class Master(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def kick(self, ctx, member: discord.Member, *, reason="We have no reason to keep you here"):
    await member.kick(reason=reason)

  @commands.command()
  async def ban(self, ctx, member: discord.Member, *, reason="Your behavior does not comply with the rules of our civilization"):
    await member.ban(reason=reason)

  @commands.command()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.mention}")
        return

def setup(client):
  client.add_cog(Master(client))