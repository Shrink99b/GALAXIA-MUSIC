#
# Copyright (C) 2021-2022 by EDWARD-ELRIC39@Github, < https://github.com/EDWARD-ELRIC39 >.
#
# This file is part of < https://github.com/EDWARD-ELRIC39/Galaxia-Music > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/EDWARD-ELRIC39/Galaxia-Music/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from GalaxiaMusic import app
from GalaxiaMusic.misc import SUDOERS
from GalaxiaMusic.utils.database import add_off, add_on
from GalaxiaMusic.utils.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@app.on_message(filters.command(VIDEOMODE_COMMAND) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
