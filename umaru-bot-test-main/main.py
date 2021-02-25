import discord
import globals

client = globals.client
client.run(TOKEN)

@client.event
async def on_ready():
	print('SUCCESSFULLY LOGGED IN AS {client.user.name.upper}'.format(client))