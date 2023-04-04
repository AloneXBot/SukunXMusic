#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class SukunBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting SukunXMusic Bot")
        super().__init__(
            "SukunXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "╭⎋ ᴜʜ ᴋᴀ ᴘʏᴀᴀʟᴀ sᴀ ʙᴏᴛ\n╰⊚ sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ\n\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @TeamSukun @sukunsupports ."
            )
        except:
            LOGGER(__name__).error(
                "ᴜʜ ᴋᴀ ᴘʏᴀᴀʟᴀ ᴄʜᴀ ʙᴏᴛ ɴᴀ ʙᴀʙʏ ʟᴏɢ ɢᴜʟᴜᴘ ᴀᴄᴄᴇss ɴᴏɪ ᴋᴀʟ ᴘᴀᴀ ʟᴀɢᴀ ʜ . ᴊᴀʟᴅɪ ᴄʜᴇ ᴊᴀᴀ ᴋᴇ ᴄʜᴇᴄᴋ ᴋᴀʟʟᴏ ʙᴀʙʏ ᴛᴜᴍɴᴇ ᴍᴜᴊʜᴇ ᴀᴅᴅ ᴛɪʏᴀ ʜ ᴋɪ ɴᴏɪ ʟᴏɢ ɢᴜʟᴜᴘ ᴍᴇ ᴀᴜʟ ᴀᴅᴍɪɴ ʙʜɪ ʙᴀɴɴᴀ ʜ ʙᴀʙʏ!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Check that bot is alive or dead"),
                        BotCommand("play", "Starts playing the requested song"),
                        BotCommand("skip", "Moves to the next track in queue"),
                        BotCommand("pause", "Pause the current playing song"),
                        BotCommand("resume", "Resume the paused song"),
                        BotCommand("end", "Clear the queue and leave voice chat"),
                        BotCommand("shuffle", "Randomly shuffles the queued playlist."),
                        BotCommand("playmode", "Allows you to change the default playmode for your chat"),
                        BotCommand("settings", "Open the settings of the music bot for your chat.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "ᴊᴀʟᴅɪ ᴄʜᴇ ᴊᴀᴀ ᴋᴇ ᴄʜᴇᴄᴋ ᴋᴀʟʟᴏ ʙᴀʙʏ ᴛᴜᴍɴᴇ ᴍᴜᴊʜᴇ ᴀᴅᴅ ᴛɪʏᴀ ʜ ᴋɪ ɴᴏɪ ʟᴏɢ ɢᴜʟᴜᴘ ᴍᴇ ᴀᴜʟ ᴀᴅᴍɪɴ ʙʜɪ ʙᴀɴɴᴀ ʜ ʙᴀʙʏ"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"SukunXMusic Bot Started as {self.name}")
