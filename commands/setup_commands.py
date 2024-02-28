from .download import download_command

def setup_commands(client):
    client.tree.command(name="download",description="Download the audio from a youtube video.")(download_command)
   
