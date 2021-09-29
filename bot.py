import os

import asyncio
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Guild
from discord.channel import TextChannel
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUID = os.getenv("DISCORD_GUILD")

# client = discord.Client()

######### Crawler Polling
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        print("Cog initialized with bot %s" % bot)
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1
        dir(bot)
        print(dir(bot))
        for guild in self.bot.guilds:
            g : Guild = guild
            for channel in g.channels:
                c : TextChannel = channel
                print(channel)
                if str(channel) == "test2":
                    await c.send("ping")
                
                #await channel.send("ping")
                #yield channel
        #await bot.channels.find("name","test2").send("Welcome!")

        #print("found channel %s" % c)
        #await self.bot.get_guild(GUID).get_channel("test2").send("Test %s" % self.index)
        #await message.channel.send("ping")



bot = commands.Bot(command_prefix=')')
bot.add_cog(MyCog(bot))

async def status_task():
    while True:
        game = discord.Game("with the API")
        await bot.change_presence(status=discord.Status.idle, activity=game)
        await asyncio.sleep(2)
        await bot.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(2)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    bot.loop.create_task(status_task())


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


bot.run(TOKEN)






# client = discord.Client()
# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)

#client.run(TOKEN)