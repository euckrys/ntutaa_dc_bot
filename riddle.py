import discord
import time
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

TOKEN = "MTE0ODU2MzQ5NzQxNjkxNzA1Mg.GD94H4.H01TlJfXm1WaQptzSqyJ0_3yy1mFu3vIUkS-3U"

num = 1

@tasks.loop(count = 10)
async def open():
    global num

    channel = client.get_channel(int(1148593649664409680))
    message = "第 " + str(num) + " 關 開關！"
    await channel.send(message)
    time.sleep(870)

    channel = client.get_channel(int(1148593649664409680))
    message = "第 " + str(num) + " 關 閉關！"
    await channel.send(message)
    time.sleep(30)
    
    channel = client.get_channel(int(1148593649664409680))
    if num != 10:
        message = "第 " + str(num) + " 關 換關！"
    else:
        message = "--------所有關卡結束--------"
    await channel.send(message)
    await channel.send("--------------------------")
    time.sleep(180)
    
    num = num+1


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "start":
        open.start()

client.run(TOKEN)