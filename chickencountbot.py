import discord
import asyncio
import sys

client = discord.Client()
f = open("count.txt","w+")
lines = f.readlines()
if(len(lines) == 2):
    dinners = int(lines[0].strip())
    lastwinner = lines[1].split()
elif len(lines) == 1:
    dinners = int(lines[0].strip())
    lastwinner = {}
else:
    dinners = 0
    lastwinner = {}
f.close()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global dinners
    global lastwinner
    if message.content.startswith('!chicken'):
        dinners = dinners + 1
        lastwinner = message.content.split(" ")[1:]
        winners = ""
        for winner in lastwinner:
            winners = winners + winner + " "
        f = open("count.txt", "w")
        f.truncate()
        f.write(str(dinners) + '\n')
        f.write(winners)
        f.close()
        await client.send_message(message.channel, 'Winner winner chicken dinner! Count is at ' + str(dinners) + '! :rooster: :fork_and_knife: ')
    elif message.content.startswith('!lastwin'):
        winners = ""
        for winner in lastwinner:
            winners = winners + winner + " "
        if len(lastwinner) == 1:
            await client.send_message(message.channel, 'The last winner was ' + winners)
        else:
            await client.send_message(message.channel, 'The last winners were ' + winners)
    elif message.content.startswith('!subtractwin'):
        dinners = dinners - 1
        await client.send_message(message.channel, 'Subtracting win')
    elif message.content.startswith('!count'):
        await client.send_message(message.channel, 'Current dinner count is ' + str(dinners) + ".")
    elif message.content.startswith('!killbot'):
        sys.exit(0)
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Commands: !chicken [winners] - !lastwin - !count - !subtractwin')

client.run('Your Key Here')
