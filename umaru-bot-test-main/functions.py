import discord
import datetime

#embed
global embed
async def embed(title = None, colour = 0xFF5733, link = None, description = None, fields = None, image = None, thumbnail = None, author = None, footer = True , timestamp = True, client = None):
    embed = discord.Embed()
    if title:
        embed.title = title
    if colour:
        embed.colour = discord.Colour(colour)
    if link:
        embed.url = link
    if description:
        embed.description = description
    if fields:
        for field in fields:
            embed.add_field(name = field[0], value= field[1], inline = field[2])
    if image:
        embed.set_image(url = image)
    if thumbnail:
        embed.set_thumbnail(url = thumbnail)
    if author:
        embed.set_author(name = author)
    if footer:
        embed.set_footer(text = client.user.name, icon_url = client.user.avatar_url)
    if timestamp:
        embed.timestamp = datetime.datetime.now()
    return embed