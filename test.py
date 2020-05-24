import logging
import struct

from discord.ext import commands

logger = logging.getLogger(__name__)


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def test(self, ctx):
        """
        Test commands for various trivial tasks
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid command passed.  Use !help.")

    @utils.command(aliases=["stol"])
    async def ping(self, ctx, params):
        """
        Converts string to long
        """
        await ctx.send("pong...")

def setup(bot):
    bot.add_cog(Test(bot))
