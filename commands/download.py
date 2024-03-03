from discord import app_commands, File, Embed
import discord
from functions.download import download_video
import shutil
import os
from urllib.parse import urlparse

@app_commands.describe(url="The link of the video to download.")
@app_commands.describe(type="The type of the content to download (Video/Audio).")
@app_commands.choices(type=[
     app_commands.Choice(name="MP4 (Video)", value="mp4"),
     app_commands.Choice(name="MP3 (Audio)", value="mp3")
])
async def download_command(interaction: discord.Interaction,url:str,type:str):

    await interaction.response.send_message(f"Downloading {type.upper()}...")
    msg = await interaction.original_response()
    await msg.fetch()
    
    if not is_youtube_url(url):
         return  await msg.edit(content="Invalid URL. please provide a valid Youtube URL")
    try:
        file_path = await download_video(url,interaction.user.id,type)
        if type == "mp4": type = "video"
        else: type = "audio"
        embed = Embed(color=0x2ECC71,type="rich",description=f"Downloaded {type} from:\n**{url}**",title="Done!")
        if msg: 
            await msg.edit(content="Content downloaded, sending it now...")
            await msg.reply(file=File(file_path))
            await msg.edit(content="",embeds=[embed])
        else:
             interaction.channel.send(file=File(file_path))
        shutil.rmtree(os.path.dirname(file_path))  # Delete the folder after sending the file
    except Exception as e:
            if msg: 
                await msg.edit(content=f"An unexpected error occurred: ```{str(e)}```")
            else:
                await interaction.channel.send(content=f"An unexpected error occurred: ```{str(e)}```")

def is_youtube_url(url):
    parsed_url = urlparse(url)
    return "youtube.com" in parsed_url.netloc or "youtu.be" in parsed_url.netloc