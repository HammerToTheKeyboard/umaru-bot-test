import discord
import random
from discord.ext import commands
from globals import TOKEN, PREFIX
from functions import embed
from lists import happylist, patlist, list1, list2

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
		text = list2[random.randint(0, len(list1)) - 1]
		embeded = await embed(description = text, client = client)
		await ctx.send(embed = embeded)
	else:
		text = list2[random.randint(0, len(list2)) - 1]
		embeded = await embed(description = text, client = client)
		await ctx.send(embed = embeded)

@client.command()
async def test(ctx):
	embeded = await embed(image = "https://media.tenor.com/images/f7293d7c20c084a37bd69e8a7cdef184/tenor.gif", client = client)
	await ctx.send(embed = embeded)

@client.command()
async def gif(ctx):
	gif = happylist[random.randint(0,len(happylist))-1]
	embeded = await embed(title = title, image = gif, client = client)
	await ctx.send(embed = embeded)

@client.command()
async def pat(ctx):
	try:
		if ctx.message.mentions:
			description = f"{ctx.author.mention} has patted {ctx.message.mentions[0].mention}! Cute!"
			gif = patlist[random.randint(0,len(patlist))-1]
			embeded = await embed(description = description, image = gif, client = client)
			await ctx.send(embed = embeded)
		else:
			description = f"You need to tell me who you want to pet."
			embeded = await embed(description=description, client = client)
			await ctx.send(embed=embeded)
	except:
		print("There was a problem with pat()")

# events
@client.event
async def on_member_join(member):
	print(f"{member.name} has joined")
	title = "Welcome!"
	description = f"{member.mention} has joined."
	embeded = await embed(title = title, description = description)
	channel = discord.utils.get(member.guild.text_channels, name="general", client = client)
	await channel.send(embed = embeded)

@client.event
async def on_member_remove(member):
	print(f'{member.name} has left')
	title = "Goodbye!"
	description = f"{member.mention} has left."
	embeded = await embed(title = title, description = description)
	channel = discord.utils.get(member.guild.text_channels, name="general", client = client)
	await channel.send(embed = embeded)

@client.event
async def on_ready():
	print('SUCCESSFULLY LOGGED IN AS', client.user.name.upper())
	title = "Hello World!"
	description = f"{client.user.name} is now online."
	embeded = await embed(title=title, description=description, client = client)
	for guild in client.guilds:
		channel = discord.utils.get(guild.text_channels, name="general")
		await channel.send(embed = embeded)

client.run(TOKEN)

