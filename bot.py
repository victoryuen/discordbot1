import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(text):
    if text.author == client.user:
        return
    
    if text.content.startswith('$hello'):
        await text.channel.send('Hello!')


client.run(os.getenv('TOKEN'))