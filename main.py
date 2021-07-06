import discord
import asyncio
import time

client = discord.Client()
token = "ODYxNzU4NDk0NzMzNjMxNTQ5.YOOdIw.0tJpnyYt5hKu2axQDd1zoPZhc1w"
key = ["옵치", "오버워치", "겐지","둠피"]


@client.event
async def on_ready():
    game = discord.Game("오버워치 재밌다!")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("login succeed")

@client.event
async def on_message(message):
    if not message.author.bot:
        for k in key:
            if not message.content.find(k) == -1:
                await message.channel.send("옵치하자!")

client.run(token)