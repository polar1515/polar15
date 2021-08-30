from logging import fatal
import discord
from discord.activity import Game
from discord.ext import commands
from discord.ext.commands import bot
import os
 
bot = commands.Bot(command_prefix='~')
 
@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity= Game("개발"))

@bot.command()
async def 핑(ctx):
 embed = discord.Embed(title=':ping_pong: 퐁!',
                       description= f'{round(bot.latency * 1000)}ms',
                       colour=0xf1c40f)
 await ctx.channel.send(embed=embed)

@bot.command()
async def 도움말(ctx):
 embed = discord.Embed(title='도움말',
                       description= '봇의 접두사는 ~ 이예요!',
                       colour=0xf1c40f)
 embed.add_field(name='> 명령어', value='도움말\r\n핑\r\n정보\r\n개발중')

 await ctx.channel.send(embed=embed)

@bot.command()
async def 정보(ctx):
 embed = discord.Embed(title='정보',
                       description= '저의 대한 정보예요!',
                       colour=0xf1c40f)
 embed.add_field(name='개발자', value='북극곰', inline=False)
 embed.add_field(name='개발 날짜', value='2021.08.30', inline=False)
 embed.add_field(name='개발자 유튜브', value='https://www.youtube.com/channel/UCR_2VeI4gEe5ELWJ2-fxmaw', inline=False)
 embed.add_field(name='서비스 국가', value='대한민국', inline=False)
     
 await ctx.channel.send(embed=embed)
 
access_token = os.environ["ODgxNjkzOTMyNDAzMTg3Nzcy.YSwjdg.3uXmAcSfsmQQMlNNVDLXjyk5AUQ"]
bot.run('access_token')
