import os
import discord
from discord.ext import commands

from myserver import server_on

intents = discord.Intents.default()
intents.members = True  # สำคัญมาก
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1483772251378683954)

    if channel:
        embed = discord.Embed(
            title="welcome to server",
            description=f"""
ยินดีต้อนรับ {member.mention}
welcome to ♪.  ALTAFAIR  ⟢₊ ˚. *!*
⠀⯎⠀⠀*!*⠀{member.mention} ⠀﹒⠀***
 ⠀<:RV:1447295941248942282><:02role:1447296966995218452>
 <:churchofgod:1447295755672096819>⠀﹐⠀⠀➷⠀<:emoji_231:1447295809488945195>
︵***⠀
 ⠀welcome   {member.mention}   ⠀﹐⠀⠀➷⠀
the person {member.guild.member_count}⠀‿⠀wlc *! *** ˚ ₊
""",
            color=discord.Color.red()
        )

        # รูปแบนเนอร์ (ใส่ลิงก์รูปเอง)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1483407902323773440/1483791975911133274/ChatGPT_Image_18_.._2569_00_28_18.png?ex=69bbe076&is=69ba8ef6&hm=663b8c85c3be49a6d1c9d57c95fc1461d4807bc1338db4a8929d0a5781b981d2&")

        # footer
        embed.set_footer(text=f"สมาชิกคนที่ {member.guild.member_count}")

        # ✅ ส่ง embed
        await channel.send(embed=embed)

server_on()

bot.run(os.getenv("TOKEN"))
