import discord
import random

from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, current_bot):
        self.bot = current_bot

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('-'))
        except Exception:
            await ctx.send('Format has to be in N-N!')
            return

        result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
        await ctx.send(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    async def repeat(self, ctx, times: int, *, content='repeating...'):
        """Repeats a message multiple times."""
        for _ in range(times):
            await ctx.send(content)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

    @commands.command()
    async def sleep(self, ctx):
        """Time to sleep"""
        await ctx.send('Z..z..z')

    @commands.group()
    async def cool(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

    @cool.command(name='bot')
    async def _bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('Yes, the bot is cool.')
