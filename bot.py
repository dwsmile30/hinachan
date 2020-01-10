import asyncio
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('히나쨩!'):
        channel = message.channel
        await channel.send('룽룽~★')

client.run("NjY1MDc4MzIwOTcwNTk2MzUz.Xhh7uw.GjrBl37pqAp3HkrQJL-GXh_j6tY")
