import discord, requests, json
from discord.ext import commands


with open("token.json") as token:
    token = json.load(token)

with open("url.json") as url:
    url = json.load(url)

with open("apikey.json") as apikey:
    url = json.load(apikey)

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print ("We have logged in as {0.user}".format(bot))

@bot.command(name = "dog")
async def send(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    data = r.json()
    if r.status_code == 200:
        print(f"API returned a {r.status_code} status.")
        await ctx.channel.send(data["message"])
    else:
        print(f"API returned a {r.status_code} status.")

bot.run(token)