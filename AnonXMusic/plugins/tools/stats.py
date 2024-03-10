import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver
import random
from pyrogram.types import InputMediaVideo

import config
from config import STATS_IMG_URL
from AnonXMusic import app
from AnonXMusic.core.userbot import assistants
from AnonXMusic.misc import SUDOERS, mongodb
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AnonXMusic.utils.decorators.language import language, languageCB
from AnonXMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS


@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_video(
        video=random.choice(["https://telegra.ph/file/22324db6f339a8c5f0cf8.mp4", "https://telegra.ph/file/f749a9259b728e02ab36b.mp4", "https://telegra.ph/file/8ac1a4012f8cd82407525.mp4", "https://telegra.ph/file/d7567e93dbea658550cea.mp4", "https://telegra.ph/file/c7a568ec0902e8cd69595.mp4", "https://telegra.ph/file/3f336920d5f2489aa595d.mp4"]),
        caption=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("stats_back") & ~BANNED_USERS)
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    await CallbackQuery.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    await CallbackQuery.answer()
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    med = InputMediaVideo(media=random.choice(["https://telegra.ph/file/4b34af77bb844c2e41239.mp4", "https://telegra.ph/file/198af582daedd89190244.mp4", "https://telegra.ph/file/d002f88c1de28db2f2398.mp4", "https://telegra.ph/file/f9b7f7e70e9fd0c7e8d1c.mp4", "https://telegra.ph/file/9232cddbe9d7906950220.mp4", "https://telegra.ph/file/e505ed1f71634cd228943.mp4"]), caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_video(
            video=random.choice(["https://telegra.ph/file/22324db6f339a8c5f0cf8.mp4", "https://telegra.ph/file/f749a9259b728e02ab36b.mp4", "https://telegra.ph/file/8ac1a4012f8cd82407525.mp4", "https://telegra.ph/file/d7567e93dbea658550cea.mp4", "https://telegra.ph/file/c7a568ec0902e8cd69595.mp4", "https://telegra.ph/file/3f336920d5f2489aa595d.mp4"]), caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(BANNED_USERS),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    med = InputMediaVideo(media=random.choice(["https://telegra.ph/file/4b34af77bb844c2e41239.mp4", "https://telegra.ph/file/198af582daedd89190244.mp4", "https://telegra.ph/file/d002f88c1de28db2f2398.mp4", "https://telegra.ph/file/f9b7f7e70e9fd0c7e8d1c.mp4", "https://telegra.ph/file/9232cddbe9d7906950220.mp4", "https://telegra.ph/file/e505ed1f71634cd228943.mp4"]), caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_video(
            video=random.choice(["https://telegra.ph/file/4b34af77bb844c2e41239.mp4", "https://telegra.ph/file/e505ed1f71634cd228943.mp4"]), caption=text, reply_markup=upl
        )
