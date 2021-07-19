from discord.ext import commands

# Testing class for basic functionality

class Test(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command(aliases=['Ping'], brief='Simple test call and response', hidden=True) #Command hidden to avoid regular use
    async def ping(self, ctx):
        await ctx.send("Pong")


def setup(bot):
    bot.add_cog(Test(bot))