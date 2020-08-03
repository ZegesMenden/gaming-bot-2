#GAMING BOT 2 VERSION 0.2.X IN DEVELOPMENT
#PATCH NOTES
#0.1 started bot, added:
#on member join dm
#help command
#trivia
#0.1 - 0.1.5, various bug fixes
#0.2 MAJOR UPDATE, added :
#profanity control
#kicking
#various bug fixed
#0.2 - 0.2.4, various small improvememnts and big fixes
#0.2.5 semi-major update, added:
#muting
#0.2.6, improved muting so that it actually fucking worked
#0.2.6.1, added timed mute
#0.2.7, added increasing mute times based on past offences, and slow removal of offences over time
#0.2.7.1, fixed trivia game

import discord
from discord.ext import commands
import time
import datetime
import csv
from datetime import datetime
from time import sleep, time
import random

last_author = ''
sender = ''
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

userdict = {
    "261325935041576960": 0, #alistair
    "351707203981541378": 0, #theo
    "239150965217820672": 0, #cam
    "444258961332502548": 0, #max
    "551593940957003778": 0, #jackson
    "556284897237663754": 0, #emily
    "648653995044241420": 0, #clayton
    "560506450829639691": 0, #nate
    "404785954579152896": 0, #painless
}

target_channel_id = 739522722169618519

#startup
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('gaming bot 2'))
    print('bot2 is online')

#dm member on join
@bot.event
async def on_member_join(ctx):
    await ctx.send('welcome to *********! to get a full list of commands, type !help in general')

#help
@bot.command()
async def help(ctx):
    await ctx.send('''It appears that you need help:
    help..................shows this message
    trivia................starts a trivia game
    ''')

#trivia
@bot.command()
async def trivia(ctx):
    question = (random.randint(1, 10))
    if question == 1:
        await ctx.send("Which videogame holds the record for having the highest budget ever to produce? 1. gta V 2. final fantasy VII 3. kingdom hearts III")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("correct!")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 1, gta V")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 1, gta V")

    if question == 2:
        await ctx.send("What is the name of the first-ever videogame? 1. pong 2. pac man 3. tennis for two")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 3, tennis for two")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 3, tennis for two")
        if answer.content == "3":
            await ctx.send("correct!")

    if question == 3:
        await ctx.send("Superstar rapper/producer Dr. Dre played an arms' dealer in which videogame? 1. 50 cent: bulletproof, 2. Dance Dance Revolution 3. Grand Theft Auto II ")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("correct!")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 1, 50 cent: bulletproof")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 1, 50 cent: bulletproof")

    if question == 4:
        await ctx.send("What is the only videogame franchise originating in the 1970's to have thus far generated over $1 billion in revenue? 1. Asteroids 2. Space Invaders 3. Pong")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 2, Space Invaders")
        if answer.content == "2":
            await ctx.send("")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 2, Space Invaders")

    if question == 5:
        await ctx.send("The original designer behind the game Tetris is from which nation? 1. Russia 2. United states, 3. Germany")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("correct!")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 1, Russia")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 1, Russia")

    if question == 6:
        await ctx.send("What is the name of the legendary videogame designer who created the Mario franchise? 1. Fusajiro Yamauchi 2. Alexey Pajitnov 3. Shigeru Miyamoto")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 3. Shigeru Miyamoto")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 3. Shigeru Miyamoto")
        if answer.content == "3":
            await ctx.send("correct!")

    if question == 7:
        await ctx.send("What is the name of the woman Mario is attempting to save from the giant ape in the original Donkey Kong? 1. Rosalina 2. Princess Peach, 3. Pauline")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 3. Pauline")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 3. Pauline")
        if answer.content == "3":
            await ctx.send("correct!")

    if question == 8:
        await ctx.send("Pokémon was originally released on which videogame console? 1. Sega Genesis, 2. Gameboy, 3. Gameboy color")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 2, Gameboy")
        if answer.content == "2":
            await ctx.send("correct!")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 2, Gameboy")

    if question == 9:
        await ctx.send("What is the name of the peripheral device that can be plugged into a Nintendo 64 controller to make it vibrate? 1. Vibratron, 2. Game Link, 3. Rumble Pak ")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("you were wrong, the correct answer was 3, Rumble Pak")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 3, Rumble Pak")
        if answer.content == "3":
            await ctx.send("correct!")

    if question == 10:
        await ctx.send("Which organization officially classified 'gaming disorder' as a mental-health condition in 2018? 1. World Health Organization, 2. Centers for Disease Control and Prevention, 3. British Broadcasting Corporation")
        answer = await bot.wait_for("message")
        if answer.content == "1":
            await ctx.send("correct!")
        if answer.content == "2":
            await ctx.send("you were wrong, the correct answer was 1, World Health Organization")
        if answer.content == "3":
            await ctx.send("you were wrong, the correct answer was 1, World Health Organization")

@bot.command()
async def clear(ctx):
    if ctx.message.author.id == "239150965217820672" or "351707203981541378":
        await ctx.send('how many lines should be purged?')
        await ctx.channel.purge(limit=int(ammount.content))

#text chat control
@bot.event
async def on_message(message):
    global current_time
    global last_author
    global messages
    global sender
    global userdict
    sender = message.author.id
    roles = ""
    roles = message.author.guild.roles
    muterole = ""
    for role in roles:
        if role.name == "Satan Spawn":
            muterole = role

    current_time = time()

    message_channel = bot.get_channel(target_channel_id)

    if time() - current_time < 1 and last_author == message.author:
        messages += 1

    else:
        messages = 0

    if messages > 5:
        
        offences = userdict[str(sender)]
        userdict[str(sender)] = offences + 1
        print("muted", sender, " for", offences * 60 + 60, " seconds")
        print(offences)
        print(offences + 1)
        messages = 0
        await message.author.add_roles(muterole)
        sleep(int(offences) * 30 + 60)
        print("unmuted", sender)
        await message.author.remove_roles(muterole)


    last_author = message.author
    current_time = time()

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    base_role = ''
    for role in member.guild.roles:
        if role.name == "his holy subject":
            base_role = role
    await member.add_roles(base_role)

#assign roles
@bot.command()
async def role(ctx):
    roles = ctx.message.author.guild.roles
    #make strings for role assignment
    defaultrole = ""
    #assign roles to strings
    for role in roles:
        if role.name == "HIS HOLY SUBJECT":
            defaultrole = role
    await ctx.message.author.add_roles(defaultrole)

bot.run('key')
