import discord
import time
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

Token = "MTE0ODU2MzQ5NzQxNjkxNzA1Mg.GweMMN.y5cuWoXooV6C8cM6npwfDFdHOY5Em_FXJ-CxVw"

num = 1

mode = input("Please choose your mode : ")
match mode:
    case 'r':
        filename = "riddle.txt"
    case 'g':
        filename = "ground.txt"
    case 't':
        filename = "test.txt"


with open(filename, mode="r") as file_object:
    MyChannelID = file_object.readline()
    MyChannelID = int(MyChannelID.strip('\n'))
    level_count = file_object.readline()
    level_count = int(level_count.strip('\n'))
    time_open = file_object.readline()
    time_open = int(time_open.strip('\n'))
    time_close = file_object.readline()
    time_close = int(time_close.strip('\n'))
    time_change = file_object.readline()
    time_change = int(time_change.strip('\n'))


@tasks.loop(count=level_count)
async def open():
    global num

    channel = client.get_channel(MyChannelID)
    message = "第 " + str(num) + " 關 開關！"
    await channel.send(message)
    time.sleep(time_open)

    channel = client.get_channel(MyChannelID)
    message = "第 " + str(num) + " 關 閉關！"
    await channel.send(message)
    time.sleep(time_close)

    channel = client.get_channel(MyChannelID)
    if num != level_count:
        message = "第 " + str(num) + " 關 換關！"
    else:
        message = "--------所有關卡結束--------"
    await channel.send(message)
    await channel.send("-------------------------------")
    time.sleep(time_change)

    num = num+1


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "$start":
        open.start()

client.run(Token)
