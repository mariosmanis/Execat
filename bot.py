import discord
import json
from discord.ext import commands

with open("config.json", "r") as f:
    data=f.read()

obj = json.loads(data)
token = str(obj["token"])

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot armed and ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@client.command(aliases=["purge"])
async def clear(ctx):
    await ctx.channel.purge()

client.run(token)
