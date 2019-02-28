import discord
import asyncio
import sys

client = discord.Client()
send_message = client.send_message

@client.event
async def on_ready():
    
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.version_info)
    print('------')
    print('Is user bot?')
    print(client.user.bot)
    print('------')

@client.event
async def on_message(message):
    
    author = message.author
    
    if message.content.startswith('.test'):
        counter = 0
        tmp = await send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'ere is some value {}.'.format(counter))
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('.play'): 
        async def joinvoice():
            #"""Joins your voice channel"""
            author = message.author
            voice_channel = author.voice_channel
            vc = await client.join_voice_channel(voice_channel)            
        await joinvoice()
    
    elif message.content.startswith('.state'):
        print(client.servers)
        for server in client.servers:
            print("[Discord] %s: %s" % (server.name, server.id))
            
            #await client.close()
    
    elif message.content.startswith('.stop'):
        async def leavevoice():
            for x in client.voice_clients:
                if(x.server == message.server):
                    return await x.disconnect()
        await leavevoice()

    elif message.content.startswith('.secret'):
        await send_message(message.channel, join)

    elif message.content.startswith('.'):
        await send_message(message.channel, 'not a command yet.')





client.run('MTk1MTI0MTM3NDExMzQ2NDM0.D1kh2g.Bu9Z2D6AFxBFdVxmA5AWghJQxQo')
