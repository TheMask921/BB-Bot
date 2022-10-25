import discord, requests, json
from discord.ext import commands
from urllib.request import urlopen

with open("token.json") as token:
    token = json.load(token)

with open("CLIENT_ID.json") as CLIENT_ID:
    CLIENT_ID = json.load(CLIENT_ID)

with open("CLIENT_SECRET.json") as CLIENT_SECRET:
    CLIENT_SECRET = json.load(CLIENT_SECRET)

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="?")

REDIRECT_URI = "https://blackboard.uwe.ac.uk/learn/api/public/v1/announcements"

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

@bot.command(name = "annou")
async def create_oauth_link(ctx):
    params = {
        "client_id" : CLIENT_ID,
        "redirect_uri" : REDIRECT_URI,
        "scope" : "user",
        "response_type" : "code",
    }
    endpoint = "https://blackboard.uwe.ac.uk/learn/api/public/v1/oauth2/authorizationcode"
    response = requests.get(endpoint, params = params)
    data2 = response.url
    if response.status_code == 200:
        print(f"API returned a {response.status_code} status.")
        await ctx.channel.send(data2)
        
    else:
        print(f"API returned a {response.status_code} status.")


bot.run(token)