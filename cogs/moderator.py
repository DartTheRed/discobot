from discord.ext import commands
import discord

from utils import controllers, notify_user

class Moderator(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot

#Kick User
   
    @commands.command(brief='Kick User', hidden=False) #Command hidden to avoid regular use
    @controllers()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = "*Thief-chan is glaring at you* You crossed the line tonight."):
        if member is not None:
            await notify_user(member, reason)
            await ctx.guild.kick(member, reason=reason)
        else:
            await ctx.send("H-uh? Which one, Boss? (No member mentioned)")

#Ban User
   
    @commands.command(brief='Ban User', hidden=False) #Command hidden to avoid regular use
    @controllers()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "*Thief-chan is glaring at you*"):
        if member is not None:
            await notify_user(member, reason)
            await ctx.guild.ban(member, reason=reason)
        else:
            await ctx.send("If you're that angry, just point me at 'em! *Sharpens knives* (No member mentioned)")

#Unban User
   
    @commands.command(brief='Unban User', hidden=False) #Command hidden to avoid regular use
    @controllers()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str ="", reason: str = "Boss says you're ok. Be grateful."):
        if member == "":
            await ctx.send("Feeling merciful today, Boss? Just let me know who! (No user as text)")
            return

        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                #await notify_user(b.user, reason)
                await ctx.send("Okay! They're back on the list!")
                return
        await ctx.send("Can't seem to find 'em, Boss. Maybe you already forgave them? (User not found)")



def setup(bot):
    bot.add_cog(Moderator(bot))