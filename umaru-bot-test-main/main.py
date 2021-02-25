import discord
from discord.ext import commands
from globals import TOKEN, PREFIX

intents = discord.Intents().all()
client = commands.Bot(command_prefix = PREFIX, case_insensitive = True, intents=intents)

# commands
@client.command()
async def ping(ctx):
    await ctx.send("pong")



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

