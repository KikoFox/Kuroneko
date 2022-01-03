import discord
from discord.ext import commands
import random
from decouple import config
import tools
from PIL import Image
from io import BytesIO


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='Kuro ', description=description, intents=intents)


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


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('-'))
    except Exception:
        await ctx.send('Format has to be in N-N!')
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def sleep(ctx):
    await ctx.send('Z..z..z')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run(config('TOKEN'))
