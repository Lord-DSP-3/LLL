import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import Message, InputMediaPhoto

from config import ADMINS
from SCHWI import app, APP, boot
import time
from HELPER import get_readable_time

@app.on_message(filters.command(["stats2", "ping2"]) & filters.user(ADMINS))
@APP.on_message(filters.command(["stats2", "ping2"]) & filters.user(ADMINS))
async def stats_global(client, message: Message):
    MSG = await message.reply_text("Loading...")
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
    uptime = get_readable_time((time.time() - boot))
    
    text = f"""
<b><u>📟 HARDWARE</b></u>
  > ᴩʟᴀᴛғᴏʀᴍ: **{sc}**
  > ʀᴀᴍ: **{ram}**
  > ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs: **{p_core}**
  > ᴛᴏᴛᴀʟ ᴄᴏʀᴇs: **{t_core}**
  > ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ: **{cpu_freq}**
  > ᴜᴘᴛɪᴍᴇ: **{uptime}**
  
<b><u>💾 STORAGE</b></u>
  > ᴀᴠᴀɪʟᴀʙʟᴇ: **{total[:4]} GiB**
  > ᴜsᴇᴅ: **{used[:4]} GiB**
  > ғʀᴇᴇ: **{free[:4]} GiB**

<b><u>💻 SOFTWARE</b></u>
  > ᴩʏᴛʜᴏɴ: **{pyver.split()[0]}**
  > ᴩʏʀᴏɢʀᴀᴍ: **{pyrover}**
"""
    await MSG.edit(text)



import asyncio
import speedtest

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("ᴄʜᴇᴄᴋɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.download()
        m = m.edit("ᴄʜᴇᴄᴋɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("ᴜᴩʟᴏᴀᴅɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spd"]) & filters.user(ADMINS))
@APP.on_message(filters.command(["speedtest", "spd"]) & filters.user(ADMINS))
async def speedtest_function(client, message):
    m = await message.reply_animation(
        animation="https://telegra.ph/file/2295b1f4737321f294e31.mp4",
        caption="ᴛʀʏɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴜᴩʟᴏᴀᴅ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ"
    )
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴩ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴩᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴩɪɴɢ:__** {result['ping']}"""
    Medit = InputMediaPhoto(media=result["share"], caption=output)
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=, caption=
    )
    
    
