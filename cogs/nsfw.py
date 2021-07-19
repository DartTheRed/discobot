import discord
from discord.ext import commands
from utils import get_momma_jokes

class NSFW(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief='Simple test call and response', hidden=False)
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_momma_jokes()
        if member is not None:
            await ctx.send("%s eat this: %s " % (member.name, insult))
        else:
            await ctx.send("%s: %s " % (ctx.message.author.name, insult))


def setup(bot):
    bot.add_cog(NSFW(bot))