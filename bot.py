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
        weather, date, time = crawl.get_weather_now()
        message_for_send = date + ' ' + time + '기준 현재 날씨입니다. \n'
        for i in weather.keys():
            message_for_send += (i + ' : ' + str(weather[i]) + '\n')

        await client.send_message(message.channel, message_for_send)
        
client.run('NDQ1NTg3NjU4OTcwODkwMjQx.Dl6iWQ.5ieRq0KZuwYyRd-Q7KTCn9yJS0k')
