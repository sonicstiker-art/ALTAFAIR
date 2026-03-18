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
    channel = member.guild.get_channel(1483772251378683954)  # ใส่ ID ห้อง
    if channel:
        await channel.send(f"ยินดีต้อนรับ {member.mention} เข้าสู่เซิร์ฟเวอร์ 🎉")

    embed = discord.Embed(
        title="🔥 WELCOME 🔥",
        description=f"""
ยินดีต้อนรับ {member.mention}

📌 อ่านกฎ: <#CHANNEL_ID>
💬 แชท: <#CHANNEL_ID>
🎮 สนุกกับเซิร์ฟได้เลย!
""",
        color=discord.Color.red()
    )

    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_image(url="https://i.imgur.com/yourimage.png")
    embed.set_footer(text=f"{member.guild.name} | สมาชิกคนที่ {member.guild.member_count}")

server_on()

bot.run(os.getenv("TOKEN"))