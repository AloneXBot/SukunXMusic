#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from pyrogram import filters

import config
from strings import get_command
from SukunXMusic import app
from SukunXMusic.misc import SUDOERS
from SukunXMusic.utils.database.memorydatabase import get_video_limit
from SukunXMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yes"
    else:
        pvt = "No"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "Yes"
    else:
        a_sug = "No"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Yes"
    else:
        down = "No"

    if not config.GITHUB_REPO:
        git = "No"
    else:
        git = f"[Repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "No"
    else:
        start = f"[Image]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "No"
    else:
        s_c = f"[Channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "No"
    else:
        s_g = f"[Group]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""⍟ **ᴍᴜsɪᴄ ʙᴏᴛ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs:**
𖢵 **<u>ʙᴀsɪᴄ ᴠᴀʀɪᴀʙʟᴇs:</u>**
  ➺ **ᴍᴜsɪᴄ_ʙᴏᴛ_ɴᴀᴍᴇ** : `{MUSIC_BOT_NAME}`
  ➺ **ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** : `{play_duration} ᴍɪɴᴜᴛᴇs`
  ➺ **sᴏɴɢ_ᴅᴏᴡɴʟᴏᴀᴅ_ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** :` {song} ᴍɪɴᴜᴛᴇs`
  ➺ **ᴏᴡɴᴇʀ_ɪᴅ** : `{owner_id}`
    
𖢵 **<u>ʀᴇᴩᴏsɪᴛᴏʀʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
  ➺ **ᴜᴩsᴛʀᴇᴀᴍ_ʀᴇᴩᴏ** : `{up_r}`
  ➺ **ᴜᴩsᴛʀᴇᴀᴍ_ʙʀᴀɴᴄʜ** : `{up_b}`
  ➺ **ɢɪᴛʜᴜʙ_ʀᴇᴩᴏ** :` {git}`
  ➺ **ɢɪᴛ_ᴛᴏᴋᴇɴ**:` {token}`

𖢵 **<u>ʙᴏᴛ ᴠᴀʀɪᴀʙʟᴇs:</u>**
  ➺ **ᴀᴜᴛᴏ_ʟᴇᴀᴠɪɴɢ_ᴀssɪsᴛᴀɴᴛ** : `{ass}`
  ➺ **ᴀssɪsᴛᴀɴᴛ_ʟᴇᴀᴠᴇ_ᴛɪᴍᴇ** : `{auto_leave} sᴇᴄᴏɴᴅs`
  ➺ **ᴀᴜᴛᴏ_sᴜɢɢᴇsᴛɪᴏɴ_ᴍᴏᴅᴇ** :` {a_sug}`
  ➺ **ᴀᴜᴛᴏ_sᴜɢɢᴇsᴛɪᴏɴ_ᴛɪᴍᴇ** : `{auto_sug} sᴇᴄᴏɴᴅs`
  ➺ **ᴀᴜᴛᴏ_ᴅᴏᴡɴʟᴏᴀᴅs_ᴄʟᴇᴀʀ** : `{down}`
  ➺ **ᴩʀɪᴠᴀᴛᴇ_ʙᴏᴛ_ᴍᴏᴅᴇ** : `{pvt}`
  ➺ **ʏᴏᴜᴛᴜʙᴇ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** : `{yt_sleep} sᴇᴄᴏɴᴅs`
  ➺ **ᴛᴇʟᴇɢʀᴀᴍ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** :` {tg_sleep} sᴇᴄᴏɴᴅs`
  ➺ **ᴄʟᴇᴀɴᴍᴏᴅᴇ_ᴍɪɴs** : `{cm} ᴍɪɴᴜᴛᴇs`
  ➺ **ᴠɪᴅᴇᴏ_sᴛʀᴇᴀᴍ_ʟɪᴍɪᴛ** : `{v_limit} ᴄʜᴀᴛs`

𖢵 **<u>ᴘʟᴀʏʟɪsᴛ ᴅᴀᴛᴀ:</u>**
  ➺ **sᴇʀᴠᴇʀ_ᴩʟᴀʏʟɪsᴛ_ʟɪᴍɪᴛ** :` {playlist_limit}`
  ➺ **ᴩʟᴀʏʟɪsᴛ_ғᴇᴛᴄʜ_ʟɪᴍɪᴛ** :` {fetch_playlist}`

𖢵 **<u>sᴩᴏᴛɪғʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
  ➺ **sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_ɪᴅ** :` {sotify}`
  ➺ **sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_sᴇᴄʀᴇᴛ** : `{sotify}`

𖢵 **<u>Playsize Vars:</u>**
  ➺ **ᴛɢ_ᴀᴜᴅɪᴏ_ғʟɪᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_aud}`
  ➺ **ᴛɢ_ᴠɪᴅᴇᴏ_ғɪʟᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_vid}`

𖢵 **<u>ᴇxᴛʀᴀ ᴠᴀʀɪᴀʙʟᴇs:</u>**
  ➺ **sᴜᴩᴩᴏʀᴛ_ᴄʜᴀɴɴᴇʟ** : `{s_c}`
  ➺ **sᴜᴩᴩᴏʀᴛ_ɢʀᴏᴜᴩ** : ` {s_g}`
  ➺ **sᴛᴀʀᴛ_ɪᴍɢ_ᴜʀʟ** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
