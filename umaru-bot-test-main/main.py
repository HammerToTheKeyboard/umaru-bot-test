import discord
import random
from discord.ext import commands
from globals import TOKEN, PREFIX
from functions import random_message, random_message1, embed, image_embed
from lists import happylist

intents = discord.Intents().all()
client = commands.Bot(command_prefix = PREFIX, case_insensitive = True, intents=intents)

known_users = ["snoopy#4548", "Shirito#0999", "𝓜𝓲𝓶𝓲#2001"]


# commands
@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command(aliases=["hi"])
async def hello(ctx):
	#await ctx.send()
	if str(ctx.author) in known_users:
		box1 = await random_message()
		await ctx.reply(box1)
	else:
		box = await random_message1()
		await ctx.reply(embed = box)

@client.command()
async def test(ctx):
	embeded = await embed(image = "https://media.tenor.com/images/f7293d7c20c084a37bd69e8a7cdef184/tenor.gif")
	await ctx.send(embed = embeded)

@client.command()
async def gif(ctx):
	title = "title"
	gif = happylist[random.randint(0,len(happylist))]
	embeded = await image_embed(title = title, image = gif)
	await ctx.send(embed = embeded)

# events
@client.event
async def on_member_join(member):
	print(f"{member.name} has joined")
	await client.get_channel(768450587909554219).send(f"{member.name} has joined!")

@client.event
async def on_member_remove(member):
	print(f'{member.name}has left')
	await client.get_channel(768450587909554219).send(f"{member.name} has left!")

@client.event
async def on_ready():
	print('SUCCESSFULLY LOGGED IN AS', client.user.name.upper())
	await client.get_channel(768450587909554219).send(f"{client.user.name} is now online!")

@client.event
async def on_error(event, args, kwargs):
	print(event, args, kwargs)


client.run(TOKEN)

