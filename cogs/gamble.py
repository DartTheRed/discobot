import random
from discord.ext import commands
import sys

class Gamble(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot



# Roll (Currently 1 - 100)

    @commands.command(aliases=['Roll'], brief='Give a random # between 1 and 100', hidden=False)
    async def roll(self, ctx):
        n = random.randrange(1, 101)
        await ctx.send(n)

# Dice Roll

    @commands.command(aliases=['Dice'], brief='Roll n number of dice with x sides', hidden=False)
    async def dice(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)]
        await ctx.send(', '.join(dice))


# Coin Flip

    @commands.command(aliases=['Coin'], brief='Flip a coin', hidden=False)
    async def coin(self, ctx):
        n = random.randrange(0, 1)
        await ctx.send("Heads" if n == 1 else "Tails")

def setup(bot):
    bot.add_cog(Gamble(bot))