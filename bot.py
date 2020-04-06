import discord
import json
import os
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print("Bot is ready")
    await la()


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, prefixes):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, ident=4)


@client.command()
async def l(extension):
    """
    Loads given extension
    """
    client.load_extension(f'cogs.{extension}')
# await ctx.send(f"Loaded {extension}")


@client.command()
async def ul(ctx, extension):
    """
    Unloads given extension
    """
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


@client.command()
async def la():
    '''
    Loads all the extensions
    '''
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await l(filename[:-3])


client.run('Njg4MTUxODk1NDk5MzQxODY0.XoUcyg.CNrYRxsCdIBm1csJffscN6l5sLI')
