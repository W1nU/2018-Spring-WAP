import discord
import asyncio
import crawl

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = '왑봇 테스트중..'))

@client.event
async def on_message(message):
    if message.content.startswith('!날씨'):
        await client.send_message(message.channel, crawl.get_weather_now())
client.run('NDQ1NTg3NjU4OTcwODkwMjQx.Dl6iWQ.5ieRq0KZuwYyRd-Q7KTCn9yJS0k')
