import discord
import random

brands=["맥 도널드","케이 에프 씨","버거 킹","노 브랜드","맥 도널드"]

with open("c:/code/dsc") as tokenfile:
    token=tokenfile.readline()

intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"로그인함 {client.user}")

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content=="/햄벅":
        await message.channel.send(random.choice(brands))

client.run(token)