import asyncio
import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message

import config
from SCHWI import app, APP
loop = asyncio.get_running_loop()

@app.on_message(filters.command("stats") & filters.group)
async def stats_global(client, message: Message):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )



@app.on_callback_query(filters.regex("bot_stats_sudo"))
async def overall_stats(client, CallbackQuery):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer("ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.", show_alert=True)
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    mod = len(ALL_MODULES)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    status = db.command("serverStatus")
    query = status["opcounters"]["query"]
    mongouptime = status["uptime"] / 86400
    mongouptime = str(mongouptime)
    total_queries = await get_queries()
    text = f"""
<b><u>📟 HARDWARE</b></u>
  > ᴍᴏᴅᴜʟᴇs: **{mod}**
  > ᴩʟᴀᴛғᴏʀᴍ: **{sc}**
  > ʀᴀᴍ: **{ram}**
  > ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs: **{p_core}**
  > ᴛᴏᴛᴀʟ ᴄᴏʀᴇs: **{t_core}**
  > ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ: **{cpu_freq}**

<b><u>💻 SOFTWARE</b></u>
  > ᴩʏᴛʜᴏɴ: **{pyver.split()[0]}**
  > ᴩʏʀᴏɢʀᴀᴍ: **{pyrover}**
  > ᴩʏ-ᴛɢᴄᴀʟʟs: **{pytgver}**

<b><u>💾 STORAGE</b></u>
  > ᴀᴠᴀɪʟᴀʙʟᴇ: **{total[:4]} GiB**
  > ᴜsᴇᴅ: **{used[:4]} GiB**
  > ғʀᴇᴇ: **{free[:4]} GiB**

<b><u>💽 DATABASE</b></u>
  > ᴜᴩᴛɪᴍᴇ: **{mongouptime[:4]} ᴅᴀʏs**
  > sɪᴢᴇ: **{datasize[:6]} ᴍʙ**
  > sᴛᴏʀᴀɢᴇ: **{storage} ᴍʙ**
  > ᴄᴏʟʟᴇᴄᴛɪᴏɴs: **{collections}**
  > ᴋᴇʏs: **{objects}**
  > ǫᴜᴇʀɪᴇs: **{query}**
  > ʙᴏᴛ ǫᴜᴇʀɪᴇs: **{total_queries}**"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )
    except Exception as e:
        await client.send_message(config.LOG_GROUP_ID, e)
        await client.send_message(config.LOG_GROUP_ID, text)
        
