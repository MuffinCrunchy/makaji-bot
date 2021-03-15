import discord
import os
import random
from discord.ext import commands
from replit import db
from keep_alive import keep_alive

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '~', intents = intents, help_command=None)

# client.remove_command("help")

@client.command()
async def help(ctx):
  embed = discord.Embed(description="Makaji is an assistant bot that can provide the best service on your discord server.\n​To get started, you can try say hi with `~hello` to greet our bot or you can use the command below", color=0xA997DF)
  embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
  embed.add_field(name="~hello", value="Say hi to our assistance bot", inline=False)
  embed.add_field(name="~ping", value="Return your ping's status", inline=False)
  embed.add_field(name="~inspire", value="Give the best words of wisdom to decorate your day", inline=False)
  embed.add_field(name="~clear", value="To delete your message's history", inline=False)

  await ctx.send(embed=embed)

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")


# player = {}

# sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# starter_encouragements = [
#   "Cheer up!",
#   "Hang in there.",
#   "You are a great person / bot!"
# ]

# if "responding" not in db.keys():
#   db["responding"] = True

# def update_encouragements(encouraging_message):
#   if "encouragements" in db.keys():
#     encouragements = db["encouragements"]
#     encouragements.append(encouraging_message)
#     db["encouragements"] = encouragements
#   else:
#     db["encouragements"] = [encouraging_message]

# def delete_encouragment(index):
#   encouragements = db["encouragements"]
#   if len(encouragements) > index:
#     del encouragements[index]
#     db["encouragements"] = encouragements

# @client.command()
# async def load(ctx, extension):
#   client.load_extension(f"cogs.{extension}")

# @client.command()
# async def unload(ctx, extension):
#   client.unload_extension(f"cogs.{extension}")

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   msg = message.content

#   if msg.startswith('.inspire'):
#     quote = get_quote()
#     await message.channel.send(quote)

#   if db["responding"]:
#     options = starter_encouragements
#     if "encouragements" in db.keys():
#       options = options + db["encouragements"]

#     if any(word in msg for word in sad_words):
#       await message.channel.send(random.choice(options))

#   if msg.startswith(".new"):
#     encouraging_message = msg.split(".new ",1)[1]
#     update_encouragements(encouraging_message)
#     await message.channel.send("New encouraging message added.")

#   if msg.startswith(".del"):
#     encouragements = []
#     if "encouragements" in db.keys():
#       index = int(msg.split(".del",1)[1])
#       delete_encouragment(index)
#       encouragements = db["encouragements"]
#     await message.channel.send(encouragements)

#   if msg.startswith(".list"):
#     encouragements = []
#     if "encouragements" in db.keys():
#       encouragements = db["encouragements"]
#     await message.channel.send(encouragements)

#   if msg.startswith(".responding"):
#     value = msg.split(".responding ",1)[1]

#     if value.lower() == "true":
#       db["responding"] = True
#       await message.channel.send("Responding is on.")
#     else:
#       db["responding"] = False
#       await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN'))