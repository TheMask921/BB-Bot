import discord, json
from octorest import OctoRest
from aiohttp import request
from discord.ext import commands


with open("token.json") as token:
    token = json.load(token)

with open("apikey.json") as apikey:
    apikey = json.load(apikey)

with open("url.json") as url:
    url = json.load(url)


intents = discord.Intents.default()

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

def make_client(url, apikey):
    try: 
        client = OctoRest(url = url, apikey = apikey)
        return client
    except ConnectionError as ex:
        print(ex)
    
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command(name = "files")
async def file_names(client):
     message = "The GCODE files currently on the printer are:\n\n"
     for k in client.files()['files']:
         message += k['name'] + "\n"
     print(message) 
    

bot.run(token)
