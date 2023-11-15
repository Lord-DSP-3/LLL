import asyncio
import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import Message

from config import ADMINS
from SCHWI import app, APP, boot
import time
from HELPER import get_readable_time

@app.on_message(filters.command(["stats2", "ping2"]) & filters.group & filters.user(ADMINS))
@APP.on_message(filters.command(["stats2", "ping2"]) & filters.group & filters.user(ADMINS))
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
    
