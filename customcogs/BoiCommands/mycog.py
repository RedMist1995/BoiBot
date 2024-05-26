from redbot.core import bank,commands
from redbot.core.utils.common_filters import normalize_smartquotes
from random import randint
from random import choice
import numpy as np
import discord
import os
import json
import pypokedex
import asyncio
import time
import pathlib
import textwrap
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from datetime import date

last_response = time.time()

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
        
    @commands.command(pass_context=True)
    async def roll(self, ctx, number : int = 100):
        """Rolls random number (between 1 and user choice)
        Defaults to 100.
        """
        author = ctx.message.author
        if number > 1:
            n = randint(1, number)
            if number == 20 and n == 20:
                await ctx.send("{} :game_die: {} :game_die: NATIONAL GEOGRAPHIC".format(author.mention, n))
            else:
                await ctx.send("{} :game_die: {} :game_die:".format(author.mention, n))
        else:
            await ctx.send("{} Maybe higher than 1? ;P".format(author.mention))
    
    @commands.command(pass_context=True)
    async def dead(self, ctx, user):
        """He's Dead Jim"""
        if user != None:
            #name = user.display_name
            await ctx.send("I can't believe " + user + " is fucking dead.")
    
    @commands.command(pass_context=True)
    async def stroke(self, ctx, user):
        if user != None:
            await ctx.send("guys " + user + " is going to give me a stroke")
    
    @commands.command(pass_context=True)
    async def hate(self, ctx, user):
        """He's Dead Jim"""
        if user != None:
            #name = user.display_name
            await ctx.send("Fuck you " + user)
    
    @commands.command(pass_context=True)
    async def bitethedust(self, ctx, user):
        """He's Dead Jim"""
        if user != None:
            n = randint(1, 3)
            if n==1:
                await ctx.send("<:killerbungle:501572309941747722> :point_right: " + user + "\n :fist: <:killerbungle:501572309941747722> :boom:")
            elif n==2:
                await ctx.send("<:killerbungle:501572309941747722> :point_right: " + user + "\n :fist: :boom: <:yeet:465643565008158741>")
            elif n==3:
                await ctx.send("<:killerbungle:501572309941747722> :point_right: " + user + "\n :fist: :boom: :boom:")
            #name = user.display_name
    
    @commands.command(pass_context=True)
    async def imagine(self, ctx, user="None"):
        """He's Dead Jim"""
        if user != "None":
            #name = user.display_name
            await ctx.send("Imagine how fun it would be to manhandle " + user + "'s tiny body. I'd just walk around the house looking for things to bend her over and fuck her on")
        else:
            await ctx.send("Imagine how fun it would be to manhandle her tiny body. I'd just walk around the house looking for things to bend her over and fuck her on")
    
    @commands.command(pass_context=True)
    async def wumbo(self, ctx, user):
        """He's Dead Jim"""
        if user != None:
            #name = user.display_name
            await ctx.send("I womba. You womba. He- she- me... womba. Womba; Wombaing; We'll have the womba; Wombarama; Wombology, The study of womba? It's first grade " + user)
    
    @commands.command(pass_context=True)
    async def teleport(self, ctx, user):
        """Nothing Personnel"""
        if user != None:
            #name = user.display_name
            await ctx.send("*Teleports behind " + user + "*\n Nothin' personnel kid.")

    @commands.command(pass_context=True)
    async def larvisafuck(self, ctx):
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/mangoes.json' , 'r+') as mango:
            mangoJson = json.load(mango)
            mangoes = mangoJson['mango']
            mangoString = f'{mangoes:,}'
            mangoes = mangoes + 1
            mangoJson['mango'] = mangoes
            mango.seek(0)
            mango.write(json.dumps(mangoJson))
            mango.truncate()
        await ctx.send("BORN TO DIE\nLARV IS A FUCK\nPun 'Em All 1989\nI am trash man\n" + mangoString + " MANGO'S PEELED")

    @commands.command(pass_context=True)
    async def pokeTeamGen(self, ctx):
        team1 = []
        team2 = []
        teamNum = []
        while len(team2) != 6:
            n = randint(1,151)
            if n not in teamNum:
                if len(team1) != 6:
                    team1.append(pypokedex.get(dex=n))
                else:
                    team2.append(pypokedex.get(dex=n))
                teamNum.append(n)
        teamString = "Team 1:\n"
        for pokemon in team1:
                teamString += pokemon.name + "\n"

        teamString += "\n Team 2:\n"

        for pokemon in team2:
                teamString += pokemon.name + "\n"

        await ctx.send(teamString)

    @commands.command(pass_context=True)
    async def pokeTeamGen2(self, ctx):
        team1 = []
        team2 = []
        teamNum = []
        while len(team2) != 6:
                n = randint(1,251)
                if n not in teamNum:
                        if len(team1) != 6:
                                 team1.append(pypokedex.get(dex=n))
                        else:
                                 team2.append(pypokedex.get(dex=n))
                        teamNum.append(n)
        teamString = "Team 1:\n"
        for pokemon in team1:
                teamString += pokemon.name + "\n"

        teamString += "\n Team 2:\n"

        for pokemon in team2:
                teamString += pokemon.name + "\n"

        await ctx.send(teamString)

    @commands.command(pass_context=True)
    async def sickToday(self, ctx):
        todaysDate = date.today()

        DIR = '/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/Sick' 
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/todaysQuote.json', 'r+') as f:
            todaysQuote = json.load(f)
            if(str(todaysDate) in todaysQuote):
                todayQuote = todaysQuote[str(todaysDate)]
                sickImage = DIR + '/' + str(todayQuote) + '.jpg'
                with open(sickImage, 'rb') as sickImageFile:
                    picture = discord.File(sickImageFile)
                    await ctx.send(file=picture)
            else:
                totalSickQuotes = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
                sickToday = randint(1, totalSickQuotes)
                #with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/sick2day.json') as f2:
                #    sickJson = json.load(f2)
                #sickImage = ""
                sickImage = DIR + '/' + str(sickToday) + '.jpg'
                with open(sickImage, 'rb') as sickImageFile:
                    picture = discord.File(sickImageFile)
                    await ctx.send(file=picture)
                todaysQuote[str(todaysDate)] = sickToday
                f.seek(0)
                f.write(json.dumps(todaysQuote))
                f.truncate()

    @commands.command(pass_context=True)
    @bank.cost(120)
    async def sickGacha(self, ctx):
        todaysDate = date.today()

        DIR = '/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/Sick' 
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/todaysQuote.json', 'r+') as f:
            todaysQuote = json.load(f)
            totalSickQuotes = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
            sickToday = randint(1, totalSickQuotes)
            sickImage = DIR + '/' + str(sickToday) + '.jpg'
            numbers = [1,2,3,4,5]
            probability = [0.5, 0.35, 0.11, 0.03, 0.01]
            rating = np.random.choice(numbers,p=probability)
            if rating == 5:
                await ctx.send('⭐')
                await ctx.send('⭐')
                await ctx.send('⭐')
                await ctx.send('⭐')
                await ctx.send('⭐')
                await ctx.send('⭐' * rating)
            else:
                await ctx.send('☆' * rating)
            with open(sickImage, 'rb') as sickImageFile:
                picture = discord.File(sickImageFile)
                await ctx.send(file=picture)
        user = ctx.author
        bal = await bank.get_balance(user)
        currency = await bank.get_currency_name(ctx.guild)
        await ctx.send(
            "{}'s balance is {} {}".format(
                user.display_name, bal, currency
            )
        )


    @commands.command(pass_context=True)
    @bank.cost(1200)
    async def sickTentPole(self, ctx):
        todaysDate = date.today()

        DIR = '/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/Sick' 
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/todaysQuote.json', 'r+') as f:
            todaysQuote = json.load(f)
            totalSickQuotes = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
            for i in range(9):
                sickToday = randint(1, totalSickQuotes)
                sickImage = DIR + '/' + str(sickToday) + '.jpg'
                numbers = [1,2,3,4,5]
                probability = [0.5, 0.35, 0.11, 0.03, 0.01]
                rating = np.random.choice(numbers,p=probability)
                if rating == 5:
                    await ctx.send('⭐')
                    await ctx.send('⭐')
                    await ctx.send('⭐')
                    await ctx.send('⭐')
                    await ctx.send('⭐')
                    await ctx.send('⭐' * rating)
                else:
                    await ctx.send('☆' * rating)
                with open(sickImage, 'rb') as sickImageFile:
                    picture = discord.File(sickImageFile)
                    await ctx.send(file=picture)
            sickToday = randint(1, totalSickQuotes)
            sickImage = DIR + '/' + str(sickToday) + '.jpg'
            await ctx.send('☆' * 4)
            with open(sickImage, 'rb') as sickImageFile:
                picture = discord.File(sickImageFile)
                await ctx.send(file=picture)
        user = ctx.author
        bal = await bank.get_balance(user)
        currency = await bank.get_currency_name(ctx.guild)
        await ctx.send(
            "{}'s balance is {} {}".format(
                user.display_name, bal, currency
            )
        )

    @commands.command(pass_context=True)
    async def sickHaiku(self, ctx):
        todaysDate = date.today()

        DIR = '/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/Sick' 
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/todaysQuote.json', 'r+') as f:
            todaysQuote = json.load(f)
            totalSickQuotes = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
            for i in range(3):
                sickToday = randint(1, totalSickQuotes)
                sickImage = DIR + '/' + str(sickToday) + '.jpg'
                with open(sickImage, 'rb') as sickImageFile:
                    picture = discord.File(sickImageFile)
                    await ctx.send(file=picture)

    @commands.command(pass_context=True)
    async def getFuckedSick(self, ctx):
        DIR = '/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/Sick' 
        with open('/home/andrew/Discord/redbot/huntteam/customcogs/BoiCommands/todaysQuote.json', 'r+') as f:
                sickImage1 = DIR + '/292.jpg'
                sickImage2 = DIR + '/291.jpg'
                with open(sickImage1, 'rb') as sickImageFile:
                    picture = discord.File(sickImageFile)
                    await ctx.send(file=picture)
                with open(sickImage2, 'rb') as sickImageFile2:
                    picture = discord.File(sickImageFile2)
                    await ctx.send(file=picture)

    @commands.command()
    async def balance(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        bal = await bank.get_balance(user)
        currency = await bank.get_currency_name(ctx.guild)
        await ctx.send(
            "{}'s balance is {} {}".format(
                user.display_name, bal, currency
            )
        )

    @commands.command()
    async def whosthatpokemon(self, ctx):
        global last_response
        pokemon = pypokedex.get(dex=randint(1,151))
        await ctx.send(pokemon.get_descriptions().get('red').replace("\n", " ").replace("\x0c"," "))

        """Wait for a correct answer, and then respond.
        Scores are also updated in this method.
        Returns False if waiting was cancelled; this is usually due to the
        session being forcibly stopped.
        Parameters
        ----------
        answers : `iterable` of `str`
            A list of valid answers to the current question.
        delay : float
            How long users have to respond (in seconds).
        timeout : float
            How long before the session ends due to no responses (in seconds).
        Returns
        -------
        bool
            :code:`True` if the session wasn't interrupted.
        """
        try:
            message = await ctx.bot.wait_for(
                "message", check=self.check_answer(ctx, pokemon.name), timeout=15.0
            )
        except asyncio.TimeoutError:
            if time.time() - last_response >= 15.0:
                await ctx.send("BZZT The Answer is " + pokemon.name)
                return False
        else:
            user = message.author
            await bank.deposit_credits(user, 120)
            reply = ("You got it {winner}! **+120** to you!").format(winner=user)
            await ctx.send(reply)
            bal = await bank.get_balance(user)
            currency = await bank.get_currency_name(ctx.guild)
            await ctx.send(
                "{}'s balance is {} {}".format(
                    user.display_name, bal, currency
                )
            )

        return True

    def check_answer(self, ctx, answer):
        """Get a predicate to check for correct answers.
        The returned predicate takes a message as its only parameter,
        and returns ``True`` if the message contains any of the
        given answers.
        Parameters
        ----------
        answers : `iterable` of `str`
            The answers which the predicate must check for.
        Returns
        -------
        function
            The message predicate.
        """

        global last_response

        def _pred(message: discord.Message):
            early_exit = message.channel != ctx.channel or message.author == ctx.guild.me
            if early_exit:
                return False

            last_response = time.time()
            guess = message.content.lower()
            guess = normalize_smartquotes(guess)
            if " " in answer and answer in guess:
                return True
            elif any(word == answer for word in guess.split(" ")):
                return True
            return False

        return _pred

    @commands.command()
    async def perryChat(self, ctx, message):
        GOOGLE_API_KEY="AIzaSyDeXisHngEqJ-jgj5dGl9PnmLnM5888weM"
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat(history=[])
        message = ("You are a chat bot with the persona of Commodore Perry. "
                   "You should respond to any text within the delimiters '{'. "
                   "Limit your responses to 150 words. " +
                   "{"+message+"}")
        response = chat.send_message(message, safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS: HarmBlockThreshold.BLOCK_NONE
        })
        await ctx.send(response)