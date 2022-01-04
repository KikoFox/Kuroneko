import discord
from discord.ext import commands
from decouple import config
import tools
from fun import Fun
from music import Music
from PIL import Image
from io import BytesIO


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='Kuro ', intents=intents)


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print(f'KuronekoBot is in {guild_count} guilds.')


@bot.event
async def on_member_join(member):

    guild = member.guild
    if guild.system_channel is not None:
        text = "Hey {0.mention}, welcome to {1.name}!\n" \
               "If you're a patron but you don't have your role assigned, DM Nope to get one".format(member, guild)
        name = member.name
        user_avatar = member.avatar_url_as(size=64)
        avt = BytesIO(await user_avatar.read())
        user_avatar = Image.open(avt)
        tools.circle_avatar(user_avatar, name)
        tools.welcome_img(name)
        await guild.system_channel.send(text, file=discord.File(f"img\profile_{name}.jpg"))


bot.add_cog(Music(bot))
bot.add_cog(Fun(bot))
bot.run(config('TOKEN'))
