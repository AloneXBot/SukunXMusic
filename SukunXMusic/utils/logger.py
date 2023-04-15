#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from SukunXMusic import app
from SukunXMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴘʀɪᴠᴀᴛᴇ ɢᴜʟᴜᴘ ʜ ɴᴏɪ ᴅᴜɴɢᴀ"
        logger_text = f"""
‌❈•≫───≪•◦ ❈ ◦•≫───≪•❈
͢ ̶̶ͥ ̶ ̶ͣ ͓ ̶͓ͫ➳⃝😻 {MUSIC_BOT_NAME}『 🇮🇳 』**ʟᴏɢɢᴇʀ**
‌❈•≫───≪•◦ ❈ ◦•≫───≪•❈

┏━━━━━━━━━━━━━━━⋗⋗
┠ **ɢᴜʟᴜᴘ ɪɴғᴏ ʙᴀʙʏ** ✨
┠━━━━━━━━━━━━━━━━⧫
┠ ɢᴜʟᴜᴘ ɴᴀᴍᴇ 🫧
┠   ┗━━ `{message.chat.title}`
┠ ɢᴜʟᴜᴘ ɪᴅ 🥰
┠   ┗━━ `{message.chat.id}`
┠ ɢᴜʟᴜᴘ ʟɪɴᴋ 😻
┠   ┗━━ {chatusername}
┠━━━━━━━━━━━━━━━━⧫
┠ **ᴜsᴇʀ ɪɴғᴏ ʙᴀʙʏ** 😘
┠━━━━━━━━━━━━━━━━⧫
┠ ᴜsᴇʀɴᴀᴍᴇ 🤭
┠   ┗━━ @{message.from_user.username}
┠ ᴜsᴇʀ ɪᴅ 🙄
┠   ┗━━ `{message.from_user.id}`
┠ ᴜsᴇʀ 🫥
┠  ┗━━ {message.from_user.mention}
┠━━━━━━━━━━━━━━━━━⧫
┠ **sᴇᴀʀᴄʜᴇᴅ ɪɴғᴏ ʙᴀʙʏ** ❤️‍🔥
┠━━━━━━━━━━━━━━━━━⧫
┠ sᴇᴀʀᴄʜᴇᴅ ❄️
┠   ┗━━ `{message.text}`
┠ sᴛʀᴇᴀᴍᴛʏᴘᴇ 💌
┠   ┗━━ {streamtype}
┗━━━━━━━━━━━━━━━⋗⋗"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
