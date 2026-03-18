import os
import discord
import asyncio  # ✅ เพิ่มตรงนี้
from discord.ext import commands

from myserver import server_on

intents = discord.Intents.default()
intents.members = True
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
    await asyncio.sleep(1)

    channel = member.guild.get_channel(1483772251378683954)

    if channel:
        embed = discord.Embed(
            title="welcome to server",
            description=f"""
ยินดีต้อนรับ {member.mention}
welcome to ♪.  ALTAFAIR  ⟢₊ ˚. *!*

👥 สมาชิก: {member.guild.member_count}
""",
            color=discord.Color.red()
        )

        embed.set_image(
            url="https://cdn.discordapp.com/attachments/1483407902323773440/1483791975911133274/ChatGPT_Image_18_.._2569_00_28_18.png"
        )

        embed.set_author(
            name=member.name,
            icon_url=member.avatar.url if member.avatar else member.default_avatar.url
        )

        await channel.send(
            content=member.mention,
            embed=embed
        )

server_on()

bot.run(os.getenv("TOKEN"))
