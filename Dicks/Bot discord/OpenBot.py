import discord
from discord.ext import commands
import youtube_dl

TOKEN = '1'
BAD_WORDS = ['Олег', '2'] 

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is online!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1301893177187504129)

    embed = discord.Embed(title = "Новый людь", description=f"{member.mention}", color = 0xffffff)

    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(bad_word in message.content for bad_word in BAD_WORDS):
        await message.delete()
        await message.channel.send(f'Сообщение удалено: {message.author.mention}, ваше сообщение содержит запрещенные слова.')

    await bot.process_commands(message)

@bot.event 
async def on_voice_state_update(member, before, after): 
    if len(after.channel.members) > 0: 
        voice = await after.channel.connect()

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send(f"{bot.user.name} прибыл {channel.mention}")
    else:
        await ctx.send("Пожалуйста подключитесь к каналу первым!")

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f'{bot.user.name} покинул голосовой канал.')

@bot.command()
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client
        
        if not voice_channel.is_connected():
            voice_channel.connect(ctx.author.voice.channel)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            url2 = info['formats'][0]['url']
            source = discord.FFmpegPCMAudio(url2, pipe=True)
            
            player = voice_channel.play(source)
            await ctx.send(f'Воспроизведение {info["title"]}')
    
    except Exception as e:
        await ctx.send(f'Произошла ошибка: {e}')

@bot.command()
@commands.has_permissions(kick_members = True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}")
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(ban_members = True, administrator=True)
async def ban(ctx, member: discord.Member, *, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}")
    await member.ban(reason=reason)

bot.run(TOKEN)