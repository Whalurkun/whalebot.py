import discord
import asyncio
import sys

client = discord.Client()
send_message = client.send_message

@client.event
async def on_ready():
    
    #test
    #users = str(len(set(bot.get_all_members())))
    #servers = str(len(bot.servers))
    #channels = str(len([c for c in bot.get_all_channels()]))
    #test-end
    
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.version_info)
    print('------')
    print('Is user bot?')
    print(client.user.bot)
    print('------')
    #print("Connected to:")
    #print("{} servers".format(servers))
    #print("{} channels".format(channels))
    #print("{} users".format(users))

@client.event
async def on_message(message):
    
    author = message.author

    if message.content.startswith('!test'):
        counter = 0
        tmp = await send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'Fuck that here is some value {}.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!play'):
        await client.join_voice_channel

    elif message.content.startswith('.'):
        await send_message(message.channel, 'not a command yet.')

    elif message.content.startswith('!hi'):
        await send_message(message.channel, 'Hello {}.'.format(author.mention))
    elif message.content.startswith('hi'):
        await send_message(message.channel, 'Hello {}.'.format(author.mention))
    elif message.content.startswith('hello'):
        await send_message(message.channel, 'Hello {}.'.format(author.mention))




client.run('MTk1MTI0MTM3NDExMzQ2NDM0.Ck6ksg.RPJSNZpSH05wP-PZTEDgGGqeNWM')


