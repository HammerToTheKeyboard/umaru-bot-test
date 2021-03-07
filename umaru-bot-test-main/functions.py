import discord
global random_message
global random_message1
import random

#list1
async def random_message():
    ind = random.randint(0,7)

    list1 = ["Hello master", "hey", "Hey senpai", "Hi snoopy", "Hey is it u !!!!!!", "Hey why are u amazing", "Hey me me hungry!!", " Hey UwU"]

    choose = list1[ind]
    return choose


#list2
async def random_message1():
    ind1 = random.randint(0, 9)

    list2 = ["and who are you", "dont talk to me human ", "shut up", "hey now fooood!!!!!! ", "who u dont talk to me", "hey shhh tim tired", "u not my parent dont need to answer you","pfft","hi do you have cola and chips","hey"]

    choose1 = list2[ind1]
    field = ["Name", choose1, False]
    result = await embed(fields = [field])
    return result

#embed
async def embed(title = None, colour = None, link = None, description = None, fields = None, image = None, thumbnail = None, author = None, footer = None):
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
        embed.set_footer(text = footer)
    return embed

#imageembed
async def image_embed(title, image):
    image_embed = await embed(title = title, image = image, colour= 0xFF5733)
    return image_embed