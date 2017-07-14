import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if 'XD' in message.content.upper():
        await client.send_message(message.channel, 'ecks dee')


client.run('MjMyMTg1ODI2NjAyMjU0MzM4.DEidAg.EO1nigROPgw1r4WpkA7r2PAXdLc')