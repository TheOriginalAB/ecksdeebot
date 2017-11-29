import discord
import asyncio

token = input()
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


client.run(token)
