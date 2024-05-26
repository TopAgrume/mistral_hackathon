import discord
from discord.ext import commands
import asyncio
import subprocess
import os
import re

# NEEDS TO BE SET WITH YOUR DISCORD TOKEN
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

process = None
process_stdout = None

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
    
    
async def read_output(channel):
    global process_stdout
    while True:
        if process_stdout:
            output = await process_stdout.readuntil(separator=b"=============\n")
            if output:
                splitted = output.decode().strip().split("\n")
                splitted = splitted[1:len(splitted) - 2]
                clean = []
                for s in splitted:
                    if not s.isspace():
                        clean.append(s)
                res = "\n".join(clean)
                res = re.sub('<.*>', '', res)
                await channel.send(f'```\n{res}\n```')
            else:
                break
        await asyncio.sleep(1)

@bot.event
async def on_message(message):
    global process, process_stdout

    if message.content.startswith('!startprocess'):
        if process is not None:
            await message.channel.send('Process is already running.')
            return

        # CHANGE THE PATHS OF MISTRAL_7B AND LORA
        command = "mistral-chat ./mistral_models/7B_instruct --max_tokens 4096 --temperature 1.0 --instruct --lora_path ./car/checkpoints/checkpoint_000100/consolidated/lora.safetensors"

        process = await asyncio.create_subprocess_shell(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process_stdout = process.stdout

        await message.channel.send('Process started.')
        bot.loop.create_task(read_output(message.channel))

    elif message.content.startswith('!input'):
        if process is None:
            await message.channel.send('No process is running.')
            return

        input_text = message.content[len('!input '):] + '\n'
        input_text = f"Generate me an ASCII art of {input_text}"
        process.stdin.write(input_text.encode())
        await process.stdin.drain()

    elif message.content.startswith('!stopprocess'):
        if process is None:
            await message.channel.send('No process is running.')
            return

        process.terminate()
        await process.wait()
        process = None
        process_stdout = None
        await message.channel.send('Process stopped.')

bot.run(TOKEN)
