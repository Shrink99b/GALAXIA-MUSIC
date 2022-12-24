#
# Copyright (C) 2021-2022 by EDWARD-ELRIC39@Github, < https://github.com/EDWARD-ELRIC39 >.
#
# This file is part of < https://github.com/EDWARD-ELRIC39/Galaxia-Music > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/EDWARD-ELRIC39/Galaxia-Music/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters

import config
from strings import get_command
from GalaxiaMusic import app
from GalaxiaMusic.misc import SUDOERS
from GalaxiaMusic.utils.database import add_off, add_on
from GalaxiaMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
