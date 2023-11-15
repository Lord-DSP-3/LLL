from pyrogram import filters

def callback_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )

import traceback
import sys 
async def handle_exception(Bot):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    tb_info = traceback.extract_tb(exc_traceback)
    filename, line_num, func_name, code = tb_info[-1]

    error_message = f"⚠️ 𝗘𝗥𝗥𝗢𝗥:\n\n"
    error_message += f"ᴄᴏᴅᴇ: **{code}**\n"
    error_message += f"ꜰɪʟᴇ: **{filename}**\n"
    error_message += f"ʟɪɴᴇ: **{line_num}**\n"
    error_message += f"ꜰᴜɴᴄᴛɪᴏɴ: **{func_name}**\n"
    error_message += f"ᴇʀʀᴏʀ: **{exc_value}**\n"
    await Bot.send_message(5329765587, error_message)

def system_reboot(UID): 
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
