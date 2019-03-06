import discord
import asyncio

client = discord.Client()

vc = None 
my_id = 174273443175464960

@client.event
async def on_ready():
    print('[INFO]: We have logged in as {0.user}'.format(client))
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    global vc
    my_user = client.get_user(my_id) 

    
    #print(message.channel.name)
    if message.author != client.user: 
        print('[INFO]: Message in [{0.guild} - #{0.channel}] from {0.author}: {1.content}'.format(message, message))
        await my_user.send('Message in [{0.guild} - #{0.channel}] from {0.author}: {1.content}'.format(message, message))
    if message.author == client.user: # Dont reply to yourself
        return

    if message.content.startswith('.test'):
        #print("USER: {0.author} has summoned us to [{0.author.voice.channel}]".format(message))
        ### Check if message is sent in a discord server or not. Otherwise I will get an error if I try to check voice state \/
        if message.guild != None:
            ### Check that the message author is in a voice channel, again to not cause any errors
            if message.author.voice != None:
                print("[INFO]: USER: {0.author} has summoned us to [{0.author.voice.channel}]".format(message))
                vc = await message.author.voice.channel.connect()
            else: 
                await message.channel.send("I cannot find you in any voice channels on this server")
        else: 
            print("[DEBUG]: User is not in any guild")
        
    if message.content.startswith('.dc'):
        await vc.disconnect()

    if message.content.startswith('.shutdown'):
        await client.close()

    try:
        if message.channel.name == "whalebot" and message.guild.name == 'valen testserv':
            valen_id = message.author.id
            await message.channel.send("You are typing in our channel, creator! Also here is your ID: "+str(valen_id))
            #print("SUCSESS")
    
    except AttributeError:
        print("[DEBUG]: Oh noes i got an error(2), probably dm-channel")
 
client.run('')
