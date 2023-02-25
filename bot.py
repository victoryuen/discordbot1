import discord
import os
cilent = discord.Cilent()

@cilent.event
async def on_ready():
    print('We have logged in as {0.user}'.format(cilent))

@cilent.event
async def on_message(text):
    if text.author == cilent.user:
        return
    
    if text.content.startswith('$hello'):
        await text.channel.send('Hello!')


cilent.run(os.getenv('TOKEN'))