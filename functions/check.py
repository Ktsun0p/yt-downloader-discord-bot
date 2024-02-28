import os 

async def get_file_size(file_path):
    size_in_bytes = os.path.getsize(file_path)
    size_in_kilobytes = size_in_bytes / 1024
    size_in_megabytes = size_in_kilobytes / 1024
    return size_in_megabytes

async def check_video_length(video_length_in_seconds):
    video_length_in_minutes = video_length_in_seconds / 60

    if video_length_in_minutes > 30:
        raise ValueError("Video is too long. Please choose a video less than 30 minutes long.")