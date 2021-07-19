import random
import aiohttp
from discord.ext import commands
import discord
import praw
from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_SUBREDDITS, REDDIT_ENABLED_NSFW_SUBREDDITS

# Testing class for basic functionality

class Images(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="Thief-chan:%s:1.0" % REDDIT_APP_ID)
        
    printSubs = ", ".join(REDDIT_ENABLED_SUBREDDITS)
    #print(printSubs)

    @commands.command(aliases=['Readit', 'ReadIt'], brief='Call a hot post from reddit.', hidden=False) #Command hidden to avoid regular use
    async def readit(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                nsfw_flag = False
                chosen_subreddit = REDDIT_ENABLED_SUBREDDITS
                if subreddit:
                    if subreddit in REDDIT_ENABLED_SUBREDDITS:
                        chosen_subreddit = subreddit
                    elif subreddit in REDDIT_ENABLED_NSFW_SUBREDDITS:
                        chosen_subreddit = subreddit
                        nsfw_flag = True
                    else:
                        await ctx.send("Uh-oh. Looks like someone blocked the hidden door. I'll have to investigate that later!")
                        await ctx.send("If it helps, the boss says these passages still work. Allowed subreddits: %s" % ", ".join(REDDIT_ENABLED_SUBREDDITS))
                        await ctx.send("The uh... *Other*... passages in the back work too... Allowed NSFW channel subreddits: %s" % ", ".join(REDDIT_ENABLED_NSFW_SUBREDDITS))
                        return

                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("HEY! We do the dirty work in the back, where some people can't see it.")
                        return


                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick = random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)
            else:
                await ctx.send("Uh-oh. Looks like someone blocked the hidden door. I'll have to investigate later!")
                await ctx.send("If it helps, the boss says these passages still work. Allowed subreddits: %s" % ", " .join(REDDIT_ENABLED_SUBREDDITS))


    @commands.command(aliases=['Cat'], brief='Get a random cat picture', hidden=False)
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("http://aws.random.cat/meow") as r:
                        data = await r.json()

                        embed = discord.Embed(title="Kitty kitty. Meow.")
                        embed.set_image(url=data['file'])
                        embed.set_footer(text="http://random.cat/")
            
                        await ctx.send(embed=embed)


    @commands.command(aliases=['Dog'], brief='Get a random dog picture', hidden=False)
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://random.dog/woof.json") as r:
                        data = await r.json()

                        embed = discord.Embed(title="Woof.")
                        embed.set_image(url=data['url'])
                        embed.set_footer(text="http://random.dog/")
            
                        await ctx.send(embed=embed)

    @commands.command(aliases=['Fox'], brief='Get a random fox picture', hidden=False)
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://randomfox.ca/floof") as r:
                        data = await r.json()

                        embed = discord.Embed(title="What does this one say?")
                        embed.set_image(url=data['image'])
                        embed.set_footer(text="https://randomfox.ca")
            
                        await ctx.send(embed=embed)                        

def setup(bot):
    bot.add_cog(Images(bot))