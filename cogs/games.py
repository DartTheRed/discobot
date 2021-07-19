import discord
import random
from discord.ext import commands

from rps.model import RPS
from rps.parser import RockPaperScissorParser
from rps.controller import RPSGame

from hangman.controller import HangmanGame

from gaw.controller import GuessAWordGame


hangman_games = {}

class Games(commands.Cog): #class creates categories in help
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command(aliases=['RPS'], usage = 'rock | paper | scissors', hidden=False)
    async def rps(self, ctx, user_choice: RockPaperScissorParser = RockPaperScissorParser(RPS.ROCK)):
        """
        Play a game of Rock Paper Scissors.

        You can only fight me, the amazing, talented, and beautiful Thief-chan!
               
        Are you quick enough?
        """
    
        game_instance = RPSGame()

        user_choice = user_choice.choice

        won, bot_choice = game_instance.run(user_choice)

        if won is None:
            message = "%s vs %s A draw? Dumb luck." % (user_choice, bot_choice)
        elif won is True:
            message = " %s vs %s What? No one is faster than me!" % (user_choice, bot_choice)
        elif won is False:
            message = " %s vs %s :smiling_imp: It's too soon for you to challenge me!" % (user_choice, bot_choice)
           
        await ctx.send(message)

    @commands.command(aliases=['Hangman', 'hm', 'HM'], brief='play a game of hangman. You have 10 guesses!')
    #@commands.dm_only()
    async def hangman(self, ctx, guess: str):
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        if game_over:
            game_over_message = "You lost! Bwahahahaha!"
            if won:
                game_over_message = "That's right! You're smarter than you look!"
                
            game_over_message = game_over_message + \
                " The correct word was %s" % hangman_instance.get_secret_word()
            await hangman_instance.reset(player_id)
            
            await ctx.send(game_over_message)
        else:
            await ctx.send("Current intel: %s" % hangman_instance.get_progress_string())
            await ctx.send("Your feeble attempts so far: %s" % hangman_instance.get_guess_string())

    @commands.group()
    async def gaw(self, ctx):
        ctx.gaw_game = GuessAWordGame()

    @gaw.command(name="start")
    async def gaw_start(self, ctx, *members: discord.Member):
        guild = ctx.guild
        author = ctx.author
        players = list()
        for m in members:
            players.append(m)

        channel = await ctx.gaw_game.start_game(guild, author, players)
        if channel is None:
            await ctx.send("Please don't try to cheat the bookies! End your other game first.")
        else:
            game = ctx.gaw_game.fetch_game()
            await ctx.send("The private room is open. No cheating! :smiling_imp:")
            await channel.send(
                "Time to start! The first category is: %s with a word length of %s" % (game.category, len(game.word)))
      
    @gaw.command(name="g")
    async def gaw_guess(self, ctx, guess: str):
        channel = ctx.channel
        author = ctx.author
        result, hint = ctx.gaw_game.guess(channel.id, guess)

        if result is None:
            await ctx.send("You are not allowed to play in this channel!")
        elif result is True:
            await ctx.send("%s you won!" % author.name)
            # start new round
            ctx.gaw_game.new_round(channel)
            new_round = ctx.gaw_game.fetch_game()
            await channel.send(
                "New Round! Category: %s with a word length of %s" % (new_round.category, len(new_round.word)))
        elif result is False and hint != "":
            await ctx.send("%s, you're close!" % author.name)


    @gaw.command(name="end")
    async def gaw_end(self, ctx):
        guild = ctx.guild
        channel = ctx.channel
        await ctx.gaw_game.destroy(guild, channel.id)

def setup(bot):
    bot.add_cog(Games(bot))