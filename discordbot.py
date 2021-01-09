import os
import ssl

from os.path import join, dirname

from discord.ext import commands
import traceback

from dotenv import load_dotenv

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pien')

@bot.command()
async def kiekie(ctx):
    await ctx.send('manji')


@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):#おはように反応
        if client.user != message.author:#自身には反応しない
            text = message.author.mention+"さんおはよう"#message.author.mentionでメンション
            await client.send_message(message.channel, text)#チャットされたチャンネルでチャットする


bot.run(token)
