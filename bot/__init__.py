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

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# array to store the channel ID who are authorized to use the bot
AUTH_CHANNEL = int(get_config(
        "AUTH_CHANNEL",
        "-100",
        should_prompt=True
    )
)
# channel/chat to join before contacting
SUB_CHANNEL = int(get_config("SUB_CHANNEL", "-100"))
# sqlalchemy Database for the bot to operate
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
#
BAN_COMMAND = get_config("BAN_COMMAND", "ban")
#
UN_BAN_COMMAND = get_config("UN_BAN_COMMAND", "unban")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# broadcast command
BROADCAST_COMMAND = get_config("BROADCAST_COMMAND", "broadcast")
# default message in-case of None types
DEFAULT_START_TEXT = (
    "Hi. ☺️\n"
    "Thank you for using me 😬\n\n"
    "This is an Open Source Project available on "
    "https://github.com/SpEcHIDe/NoPMsBot\n\n\n"
    "If you are the owner of this bot, "
    "and are seeing this message 🤦‍♂️, "
    "means that you have not set up "
    "the ENVironment variables properly "
    "for the bot to function.\n\n\n"
    "ℹ️ Subscribe @SpEcHlDe if you 😍 using this bot❗️❣️"
)
# /start message when other users start your bot
START_OTHER_USERS_TEXT = int(get_config(
    "START_OTHER_USERS_TEXT",
    0
))
# check online status of your bot
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        "i am online <b>master</b>\n\n"
        "This is an Open Source Project available on "
        "https://github.com/SpEcHiDe/NoPMsBot\n\n\n"
        "ℹ️ Subscribe @SpEcHlDe if you 😍 using this bot❗️❣️"
    )
)
# message to indicate,
# if any message was deleted by the user
# so as to prevent replying to that message
DELETED_MESSAGES_NOTIFICATION_TEXT = get_config(
    "DELETED_MESSAGES_NOTIFICATION_TEXT",
    (
        "this message was deleted\n\n"
        "This is an Open Source Project available on "
        "https://github.com/SpEcHiDe/NoPMsBot\n\n\n"
        "ℹ️ Subscribe @SpEcHlDe if you 😍 using this bot❗️❣️"
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)

START_MSG = get_config(
    "START_MSG",
    "Hai 🙋🏻‍♂️, Apa kabar?\n\nSaya adalah bot yang terhubung langsung dengan 𝗮𝗱𝗺𝗶𝗻 𝗡𝗦𝗜𝗗. Diciptakan untuk melayani kalian yang ingin gabung 𝗩𝗩𝗜𝗣 𝗡𝗦𝗜𝗗.\n\nSilahkan tekan /vip untuk melihat daftar harga. Mohon tunggu dan bersabar chat kalian pasti akan dibalas admin 😇"
) 


VIP_MSG = get_config(
     "VIP_MSG", 
     "🎥𝙻𝙸𝚂𝚃 𝙶𝚁𝚄𝙿 𝙱𝙾𝙺*𝙿 𝚃𝙰𝙽𝙿𝙰 𝙻𝙸𝙽𝙺⬇️\n\n𝟷. 🔐𝚅𝚅𝙸𝙿 𝙲𝙰𝙼𝙿𝚄𝚁𝙰𝙽🔞 = 𝚁𝚙 𝟺𝟶.𝟶𝟶𝟶\n✅𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙲𝙰𝙼𝙿𝚄𝚁𝙰𝙽\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝙱𝙴𝙻𝙰𝚂𝙰𝙽 𝚁𝙸𝙱𝚄 𝚅𝙸𝙳𝙴𝙾\n\n𝟸. 🔐𝚅𝙸𝙿 𝚁𝙰𝚁𝙴 🔞 = 𝚁𝚙 𝟹𝟶.𝟶𝟶�\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝚁𝙰𝚁𝙴\n\n𝟹. 🔐𝚅𝙸𝙿 𝙾𝙽𝙻𝚈𝙵𝙰𝙽𝚂 🔞 = 𝚁𝚙 𝟹𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙾𝙽𝙻𝚈𝙵𝙰𝙽𝚂\n\n𝟺. 🔐𝚅𝙸𝙿 𝙷𝙸𝙹𝙰𝙱 🔞 = 𝚁𝚙 𝟹𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙷𝙸𝙹𝙰𝙱\n\n𝟻. 🔐𝚅𝙸𝙿 𝙻𝙸𝚅𝙴 (𝙾𝙼𝙴 𝙱𝙸𝙶𝙾 𝙳𝙻𝙻/𝚅𝙲𝚂) 🔞 = 𝚁𝚙 𝟹𝟶.𝟶𝟶𝟶\n✅𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝚅𝙴 𝙱𝙸𝙶𝙾 𝙾𝙼𝙴 / 𝚅𝙲𝚂\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝚅𝙸𝙳𝙴𝙾\n\n𝟼. 🔐𝚅𝙸𝙿 𝙸𝙽𝙳𝙾 🔞 = 𝚁𝚙 𝟻𝟶.𝟶𝟶𝟶\n✅𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙸𝙽𝙳𝙾 𝙼𝙰𝙻𝙰𝚈\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝙱𝙴𝙻𝙰𝚂𝙰𝙽 𝚁𝙸𝙱𝚄 𝚅𝙸𝙳𝙴𝙾\n\n𝟽. 🔐𝚅𝙸𝙿 𝙹𝙰𝚅 🔞  = 𝚁𝚙 𝟹𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙹𝙰𝚅\n\n𝟾.🔐𝚅𝙸𝙿 𝙱𝙾𝙲𝙸𝙻 🔞  = 𝚁𝚙 𝟻𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙱𝙾𝙲𝙸𝙻\n\n𝟿. 🔐𝚅𝙸𝙿 𝙱𝙰𝚁𝙰𝚃 🔞  = 𝚁𝚙 𝟹𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙸𝙱𝚄𝙰𝙽 𝙵𝚄𝙻𝙻 𝚅𝙸𝙳𝙴𝙾 𝙱𝙰𝚁𝙰𝚃\n\n𝟷𝟶. 🔐𝚅𝙸𝙿 𝙷𝙴𝙽𝚃𝙰𝙸 🔞  = 𝚁𝚙 3𝟶.𝟶𝟶𝟶\n✅𝙱𝙴𝚁𝙸𝚂𝙸 𝚁𝙰𝚃𝚄𝚂𝙰𝙽 𝚅𝙸𝙳𝙴𝙾 𝙷𝙴𝙽𝚃𝙰𝙸\n\n_𝚋𝚎𝚛𝚕𝚊𝚔𝚞 𝚞𝚗𝚝𝚞𝚔 𝚜𝚎𝚖𝚞𝚊 𝚐𝚛𝚞𝚙\n✅𝚂𝙴𝙺𝙰𝙻𝙸 𝙱𝙰𝚈𝙰𝚁 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽\n✅𝙳𝙰𝙿𝙰𝚃 𝙹𝙰𝙼𝙸𝙽𝙰𝙽 𝙸𝙽𝚅𝙸𝚃𝙴 𝚄𝙻𝙰𝙽𝙶 𝙹𝙸𝙺𝙰 𝙲𝙷 𝙺𝙴𝙱𝙰𝙽𝙽𝙴𝙳\n✅𝙱𝙴𝙱𝙰𝚂 𝙰𝙺𝚂𝙴𝚂 𝙽𝙾 𝙻𝚄𝙰𝚁 𝙰𝚃𝙰𝚄 𝙸𝙽𝙳𝙾\n✅𝚄𝙿𝙳𝙰𝚃𝙴 𝚂𝙴𝚃𝙸𝙰𝙿 𝚂𝙰𝙰𝚃\n\n🎉𝙹𝙾𝙸𝙽 𝚂𝙴𝙼𝚄𝙰 𝙶𝚁𝚄𝙿 = 𝚁𝚙 𝟸𝟶𝟶.𝟶𝟶\n\n𝙋𝙖𝙮𝙢𝙚𝙣𝙩:\n✅DANA ✅𝙶𝙾𝙿𝙰𝚈  ✅BANK BSI ✅OVO ✅SHOPE PAY\n\n𝚃𝙴𝚂𝚃𝙸 𝙳𝙰𝙽 𝙹𝙾𝙸𝙽 ? : @VvipNSID02\n\n𝙼𝙰𝚄 𝙶𝙰𝙱𝚄𝙽𝙶? 𝙲𝙷𝙰𝚃 𝙺𝙴 👇\n@ChatJoinVipBot\n@ChatJoinVipBot\n@ChatJoinVipBot"
) 

# message to show when user is banned
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "You have been <b>banned</b> forever.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# IDEKWBYRW
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
# message to show when user is unbanned
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "You have been <b>un-banned</b>.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "NoPMsBot.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)
