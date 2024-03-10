import random 
import asyncio 
from pyrogram import filters
from pyrogram.types import Message 
from AnonXMusic import app 
from config import BANNED_USERS 

# Assuming you have a list of video URLs 
VIDEO_LIST = [ 
    "https://telegra.ph/file/63754311ff1924451321a.mp4", 
    "https://telegra.ph/file/bb341bf4dc85bd1a2b713.mp4", 
    "https://telegra.ph/file/674b61466ac9496abf318.mp4", 
    # Add more video URLs as needed 
] 

@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"]) & ~BANNED_USERS) 
async def sudoers_list(client, message: Message): 
    try: 
        # Option: Send a random video with 'has_spoiler=True'
        random_video = random.choice(VIDEO_LIST) 

        await message.reply_video(video=random_video, has_spoiler=True) 
  
    except Exception as e: 
        await message.reply_text(f"Error: {e}")
