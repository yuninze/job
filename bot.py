import discord

import random
from collections import Counter

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
    hmbg_brands=["맥 도널드","케이 에프 씨","버거 킹","썹","노 브랜드"]
    hmbg_brands_chosen_cache=[]
    if message.author==client.user:
        return
    if message.content=="/햄버거":
        hmbg_chosen:str=random.choice(hmbg_brands)
        hmbg_brands_chosen_cache.append(hmbg_choice)
        hmbg_brands_chosen_counts:dict=Counter(hmbg_brands_chosen_cache)
        await message.channel.send(
            f"햄버거::{chosen} (지금까지 {hmbg_brands_chosen_counts[chosen]}번 나왔음)")
        
client.run(token)