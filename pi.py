import os
import asyncio

async def starta():
	print("starting up (ongk)")
	await [q for q in os.walk("e:/ongk/")]

async def startb():
	print("starting up (dnld)")

asyncio.run(starta())
asyncio.run(startb())