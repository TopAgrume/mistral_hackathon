import discord
from discord.ext import commands

# export in env and import
TOKEN = 'MTI0MzkxMTUwODY5MDQ3MzA2MQ.GAJEpl.1KtK_g12g84dbx0VagacdBvtytKH2WHRDjDRWw'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='small-ascii')
async def ping(ctx):
    await ctx.send("``` /\_/\ \n( o.o )\n > ^ < ```")

@bot.command(name='big-ascii')
async def big_ascii(ctx):
    await ctx.send("``` (\"`-''-/\").___..--''\"`-._ \n `6_ 6  )   `-.  (     ).`-.__.`) \n (_Y_.)'  ._   )  `._ `. ``-..-' \n   _..`--'_..-_/  /--'_.' \n  ((((.-''  ((((.'  (((.-'  ```")

bot.run(TOKEN)