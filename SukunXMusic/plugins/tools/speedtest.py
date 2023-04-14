#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import speedtest
from config import MUSIC_BOT_NAME
from pyrogram import filters
from strings import get_command
from SukunXMusic import app
from SukunXMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("ᴄʜᴇᴄᴋ ᴋᴀʟ ʟᴀʜɪ ʜᴜ sᴘᴇᴇᴅ ʙᴀʙʏ")
        test.download()
        m = m.edit("ᴜᴘʟᴏᴀᴅ ᴋᴀʟᴛɪ ʜᴜ ᴍᴇʟᴀ ʙᴀᴄʜᴀ")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit(".............")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("ᴄʜᴇᴄᴋ ᴋᴀʟ ʟᴀʜɪ ʜᴜ sᴘᴇᴇᴅ ʙᴀʙʏ")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**{MUSIC_BOT_NAME} sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
𖢵 <u>**ᴄʟɪᴇɴᴛ:**</u>
  ➺ **__ɪsᴩ:__** {result['client']['isp']}
  ➺ **__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
𖢵 <u>**sᴇʀᴠᴇʀ**</u>

  ➺ **__ɴᴀᴍᴇ:__** {result['server']['name']}
  ➺ **__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
  ➺ **__sᴩᴏɴsᴏʀ:__** {result['server']['sponsor']}
  ➺ **__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
  ➺ **__ᴩɪɴɢ:__** {result['ping']}
"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
