from commands.setup_commands import setup_commands
from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from typing import Final

load_dotenv()

TOKEN:Final[str] = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix=".")

setup_commands(client)

@client.event
async def on_ready():
    await client.tree.sync()
    custom = discord.CustomActivity("ROACH IGNACIO 🪳🪳🔥🔥")
    await client.change_presence(status=discord.Status.dnd, activity=custom)
    print(f'{client.user} is ready')

@client.event
async def on_command_error(ctx, error):
    return
#test
def main():
    client.run(TOKEN)

if __name__=='__main__':
    main()
