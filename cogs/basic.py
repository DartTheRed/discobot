from discord.ext import commands
from utils import text_to_owo
import discord
import requests
import json
import random
from utils import notify_user
from settings import *

class Basic(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot
    
    #@commands.command(brief ='provide args', hidden=True)
    #async def sample(ctx, *args):
    #    if len(args) > 0:
    #        await ctx.send(", ".join(args))
    #    else:
    #        await ctx.send("please refer to help")

    @commands.command(aliases=['Hello', 'Hi', 'hi'], brief='Hello')
    async def hello(self, ctx):
        with open(os.path.join(IMAGE_THIEF, "thief-intro.jpg"), 'rb') as f:
            img = discord.File(f)
            reply = f"Hey there, {ctx.author.mention}!"

            await ctx.send(reply, file=img)
    
    @commands.command(brief='Create invite good for 1 hour')
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=3600)
        await ctx.send(link)

    @commands.command(help = 'Poke a member')
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Uhhh, who? You messing with me? (No member poked)")

    @commands.command(help = 'Slap a member with a fish')
    async def fish(self, ctx, member: discord.Member = None):
        if member is not None:
            message = "%s slaps %s with a :fish:" % (ctx.author.name, member.mention)
            await ctx.send(message)
        else:
            await ctx.send("Uhhh, who? You messing with me?")

    @commands.command(aliases=['duel', 'Fight', 'Duel'], description='Challenge another user with Thief-chan as your referee')
    async def fight(self, ctx, *, member: discord.Member):
        '''Challenge another user with Thief-chan as your referee'''
        await ctx.send(":crossed_swords:")
        await ctx.send("Weapons have been drawn...***ARE YOU READY?!?*** :boxing_glove:")
        if member != self.bot.user:
            winner = random.choice([True, False])
            if winner:
                await ctx.send(f"{ctx.message.author.display_name} pummels {member.display_name}. {ctx.message.author.display_name} wins.\n:trophy:")
            else:
                await ctx.send(f"{ctx.message.author.display_name} attacks {member.display_name}, but it quickly goes poorly for them. {ctx.message.author.display_name} is defeated.\n:head_bandage:")
        else:
            await ctx.send(f"{self.bot.user.mention} laughs maniacally at {ctx.message.author.mention}'s attempt to usurp her, before promptly pummeling them into defeat! :triumph:")
            await ctx.message.add_reaction('✅')
        if ctx.guild:
            await ctx.message.delete(delay=15)

    @commands.command(name='owo', hidden = True)
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command(name='inspire', aliases=['Inspire'], help='Provides a random inspirational quote')
    async def post_quote(self, ctx):
        #Inspiration Quote API
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" +json_data[0]['a']
        #Return Quote
        await ctx.send(quote)

def setup(bot):
    bot.add_cog(Basic(bot))