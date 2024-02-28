from pytube import YouTube
import os 
import shutil
from .check import get_file_size, check_video_length

async def download_audio(url:str,user:int):
    mp3_link = url
    audio = YouTube(mp3_link)

    await check_video_length(audio.length)

    try:
        output = audio.streams.get_audio_only().download()
        base, ext = os.path.splitext(output)
        new_file = base+".mp3"
        os.rename(output,new_file)

        # Create a folder with the USER ID as name inside the folder "files"
        user_folder = os.path.join("temp_files", str(user))
        os.makedirs(user_folder, exist_ok=True)

        # Move the downloaded file to the correct folder
        user_file_path = os.path.join(user_folder, os.path.basename(new_file))
        os.rename(new_file, user_file_path)
        size = await get_file_size(user_file_path)
        if size > 25: 
            shutil.rmtree(os.path.dirname(user_file_path))
            raise ValueError(f"File size is {size} MB, can't be sent.\nMB limit is 25.00.")
        return user_file_path
    except Exception as e:
          raise ValueError(e)  