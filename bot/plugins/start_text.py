#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from bot import (
    AUTH_CHANNEL,
    COMMM_AND_PRE_FIX,
    START_MSG,
    START_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler


@Bot.on_message(
    filters.command("start", "/") &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def num_start_message(client: Bot, message: Message):
        buttons = [
            [
                InlineKeyboardButton("Info & Testi VIP", url="https://t.me/VvipNSID02"),
            ]
        ]
        await message.reply_photo(
                "https://telegra.ph//file/b3da13ddeb799d8f06ffe.jpg", 
            caption=START_MSG, 
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
        )
