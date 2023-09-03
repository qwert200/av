from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url=f"https://t.me/Backup_Bosss"),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", callback_data="gib_support"
            )
            InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ", callback_data="gib_source")
        ],
    ]
    return buttons
