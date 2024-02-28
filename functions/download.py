from pytube import YouTube
import os 
import shutil
from .check import get_file_size, check_video_length

async def download_video(video_link:str,user:int,type:str):

    video = YouTube(video_link)

    await check_video_length(video.length)

    try:
        if type == "mp3": 
            output = video.streams.get_audio_only().download()
        else:
            output = video.streams.get_highest_resolution().download()

        base, ext = os.path.splitext(output)
        new_file = base+f".{type}"
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

