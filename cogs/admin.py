from discord.ext import commands
import discord
import datetime
import os
from settings import *
from utils import controllers



# Testing class for basic functionality

class Admin(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot

# COG LISTENER

    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        print(e)
        await ctx.send("Please check the thief's handbook (!help) for proper resource deployment or talk to the boss!")
        await ctx.message.add_reaction('❌')   

# UNLOAD

    @commands.command(brief='Use cogs.CATEGORY')
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("I think it's stuck, Boss. (Could not unload)")
            return
        await ctx.send("Now what do I do with it? Into the junk pile, I guess! (Cog unloaded)")

# LOAD

    @commands.command(brief='Use cogs.CATEGORY')
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("I think this part goes here. *BOOM!* Uh... (Could not load)")
            return
        await ctx.send("Good as new! (Cog loaded)")

# RELOAD

    @commands.command(brief='Use cogs.CATEGORY')
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Is it supposed to make noises like this? (Reload Failed)")
            return
        await ctx.send("Nothin' a little reboot couldn't fix! (Cog reloaded)")

    
    #@commands.is_owner() #@commands.has_role("Mods") #@commands.check(commands.is_owner()) #@commands.check_any(commands.is_owner(), commands.has_role("Moderator")) @controllers()


    @commands.command(aliases=['Status'], brief='Get some basic server info')
    @controllers()
    async def status(self, ctx, *args):
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        memCount = guild.member_count

        embed = discord.Embed(description="Server Status", color=discord.Color.blue())
        #file = discord.File(os.path.join(IMAGE_THIEF, "thief-intro.jpg"), filename="image.png")
        file = discord.File(os.path.join(IMAGE_THIEF, "thief-profile.jpg"), filename="image.png")
        embed.set_thumbnail(url="attachment://image.png")
        embed.set_image(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6887410c-e719-4ec4-83ae-bf3704b72ef0/dp2gvv-9b360a46-7907-444c-b628-cfaf7769a8b6.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjg4NzQxMGMtZTcxOS00ZWM0LTgzYWUtYmYzNzA0YjcyZWYwXC9kcDJndnYtOWIzNjBhNDYtNzkwNy00NDRjLWI2MjgtY2ZhZjc3NjlhOGI2LmpwZyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl19.ZZGt05GakvGrKAv0kNxjNxJqCDosRyU1fSdUdbyzdFI")
        
        embed.add_field(name="Server Name", value=guild.name, inline=False) #default = true
        embed.add_field(name="# of Text Channels", value=no_text_channels)
        embed.add_field(name="# of Voice Channels", value=no_voice_channels)
        embed.add_field(name="# of Members", value=memCount, inline=False)
        embed.add_field(name="AFK Channel", value=guild.afk_channel, inline=False)

        emoji_string = ""
        for emoji in guild.emojis:
            if emoji.is_usable():
                emoji_string += str(emoji)
        embed.add_field(name="Custom Emojis", value=emoji_string or "Nothing here. Stop being lazy, Boss!", inline=False)

        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send("Reporting in, Boss!")
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))