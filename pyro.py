import os
import json
import time
import asyncio

from asyncio.exceptions import TimeoutError

from pyromod import listen
from pyrogram.types import(
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import(
    FloodWait,
    ApiIdInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    UserNotParticipant,
    PhoneNumberInvalid,
    SessionPasswordNeeded
)
from pyrogram import filters
from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import(
    PeerIdInvalid,
    ChatAdminRequired,
    UserNotParticipant,
    UsernameNotOccupied
)

from Ultron import Var
from Ultron import Ultron

SUPPORT = Var.SUPPORT
SUPPORT_GROUP = Var.SUPPORT_GROUP

support = SUPPORT
group = SUPPORT_GROUP
bot = "@UltronPyro_Bot"
bot_name = "UltronPyro_Bot"
owner = "Warning_MadBoy_is_Back"
dev = "ItS_PRaNAv_Xd"

GREETING = """👋🏻 **𝑯𝒆𝒚𝒂!! {}**, 𝑰❜𝒎 **PʏʀᴏGʀᴀᴍ Sᴛʀɪɴɢ Sᴇssɪᴏɴ Gᴇɴᴇʀᴀᴛᴏʀ**\n𝑰 𝒄𝒂𝒏 𝒉𝒆𝒍𝒑 𝒚𝒐𝒖 𝒕𝒐 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒆 𝒂 𝑷𝒚𝒓𝒐𝑮𝒓𝒂𝒎 𝑺𝒕𝒓𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒇𝒐𝒓 𝒚𝒐𝒖𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑨𝒄𝒄𝒐𝒖𝒏𝒕 𝒊𝒏 𝒂𝒏 𝑬𝒂𝒔𝒚 𝑾𝒂𝒚...\n\n𝑷𝒍𝒆𝒂𝒔𝒆 𝒔𝒆𝒏𝒅 𝒚𝒐𝒖𝒓 `𝘼𝙋𝙄_𝙄𝘿` 𝒇𝒐𝒓 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝑺𝒆𝒔𝒔𝒊𝒐𝒏.\n𝑮𝒆𝒕 𝒕𝒉𝒊𝒔 𝒗𝒂𝒍𝒖𝒆 𝒇𝒓𝒐𝒎 **[𝙃𝙚𝙧𝙚](https://my.telegram.org)**."""

HASH = """**__Nᴏᴛᴇᴅ!!__**\n\n𝑵𝒐𝒘 𝒔𝒆𝒏𝒅 𝒚𝒐𝒖𝒓 `𝘼𝙋𝙄_𝙃𝘼𝙎𝙃` 𝒊𝒏 𝒐𝒓𝒅𝒆𝒓 𝒕𝒐 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆.\n𝑮𝒆𝒕 𝒕𝒉𝒊𝒔 𝒗𝒂𝒍𝒖𝒆 𝒇𝒓𝒐𝒎 **[𝙃𝙚𝙧𝙚](https://my.telegram.org)**.\n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒑𝒓𝒆𝒔𝒔 /cancel 𝒊𝒇 𝒚𝒐𝒖 𝒅𝒐𝒏❜𝒕 𝒘𝒂𝒏𝒏𝒂 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔."""

NUMBER = """**__Nᴏᴛᴇᴅ!!__**\n\n𝑵𝒐𝒘 𝒔𝒆𝒏𝒅 𝒚𝒐𝒖𝒓 `𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘼𝙘𝙘𝙤𝙪𝙣𝙩❜𝙨 𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧` 𝒊𝒏 𝒐𝒓𝒅𝒆𝒓 𝒕𝒐 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒇𝒖𝒓𝒕𝒉𝒆𝒓.\n**𝑷𝒍𝒆𝒂𝒔𝒆 𝒏𝒐𝒕𝒆 𝒕𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒑𝒐𝒊𝒏𝒕𝒔 𝒃𝒆𝒇𝒐𝒓𝒆 𝒆𝒏𝒕𝒆𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝑷𝒉𝒐𝒏𝒆 𝑵𝒖𝒎𝒃𝒆𝒓 :**\n\n- 𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙩𝙝𝙚 𝙣𝙪𝙢𝙗𝙚𝙧 𝙮𝙤𝙪❜𝙧𝙚 𝙚𝙣𝙩𝙚𝙧𝙞𝙣𝙜 𝙚𝙭𝙞𝙨𝙩𝙨 𝙬𝙞𝙩𝙝 𝙖 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘼𝙘𝙘𝙤𝙪𝙣𝙩.\n- 𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙩𝙝𝙚 𝙣𝙪𝙢𝙗𝙚𝙧 𝙚𝙣𝙩𝙚𝙧𝙚𝙙 𝙞𝙨 𝙞𝙣 𝙄𝙣𝙩𝙚𝙧𝙣𝙖𝙩𝙞𝙤𝙣𝙖𝙡 𝙁𝙤𝙧𝙢𝙖𝙩, **𝙀𝙭:~** `+91 69696 96969` 𝙤𝙧 `+1 96969 69696` 𝙤𝙧 𝙖𝙣𝙮 𝙤𝙩𝙝𝙚𝙧 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 𝘾𝙤𝙙𝙚\n- 𝘿𝙤𝙣❜𝙩 𝙨𝙩𝙚𝙖𝙡 𝙖𝙣𝙮𝙤𝙣𝙚❜𝙨 𝙚𝙡𝙨𝙚 𝙣𝙪𝙢𝙗𝙚𝙧.\n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒑𝒓𝒆𝒔𝒔 /cancel 𝒊𝒇 𝒚𝒐𝒖 𝒅𝒐𝒏❜𝒕 𝒘𝒂𝒏𝒏𝒂 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔."""

CONFIRMATION = """**__Nᴏᴛᴇᴅ!!__**\n\n𝑩𝒖𝒕 𝒃𝒆𝒇𝒐𝒓𝒆 𝒈𝒐𝒊𝒏𝒈 𝒂𝒉𝒆𝒂𝒅, 𝑰 𝒏𝒆𝒆𝒅 𝒕𝒉𝒆 𝒄𝒐𝒏𝒇𝒊𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒕𝒉𝒂𝒕 𝒊𝒇 𝒕𝒉𝒆 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅 `𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧` 𝒊𝒔 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒐𝒓 𝒏𝒐𝒕!!\n\n- 𝙄𝙛 𝙩𝙝𝙚 `𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧` 𝙞𝙨 𝙘𝙤𝙧𝙧𝙚𝙘𝙩:\nSᴇɴᴅ `y`\n\n- 𝙀𝙡𝙨𝙚:\nSᴇɴᴅ `n`\n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒑𝒓𝒆𝒔𝒔 /cancel 𝒊𝒇 𝒚𝒐𝒖 𝒅𝒐𝒏❜𝒕 𝒘𝒂𝒏𝒏𝒂 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔."""

OTP = """**__Nᴏᴛᴇᴅ!!__**\n\n𝑨𝒏 `𝙊𝙏𝙋` 𝒘𝒂𝒔 𝒔𝒆𝒏𝒕 𝒕𝒐 𝒚𝒐𝒖𝒓 `𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧`,\n𝑷𝒍𝒆𝒂𝒔𝒆 𝒆𝒏𝒕𝒆𝒓 𝒕𝒉𝒆 `𝙊𝙏𝙋` 𝒊𝒏 𝒕𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒇𝒐𝒓𝒎𝒂𝒕 :~ `1 2 3 4 5` __(𝙎𝙥𝙖𝙘𝙚 𝙗𝙚𝙩𝙬𝙚𝙚𝙣 𝙚𝙖𝙘𝙝 𝙣𝙪𝙢𝙗𝙚𝙧.)__\n\n𝑰𝒇 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆𝒏❜𝒕 𝒓𝒆𝒄𝒆𝒊𝒗𝒆𝒅 𝒂𝒏𝒚 `𝙊𝙏𝙋`, 𝒕𝒉𝒆𝒏 𝒕𝒓𝒚 𝒂𝒏𝒅 𝑮𝒐-𝑨𝒉𝒆𝒂𝒅 𝒔𝒕𝒂𝒓𝒕𝒊𝒏𝒈 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏 𝒘𝒊𝒕𝒉 /start 𝒄𝒐𝒎𝒎𝒂𝒏𝒅.\n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒑𝒓𝒆𝒔𝒔 /cancel 𝒊𝒇 𝒚𝒐𝒖 𝒅𝒐𝒏❜𝒕 𝒘𝒂𝒏𝒏𝒂 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔."""

TWO_STEP_VERIFICATION = """**__Nᴏᴛᴇᴅ!!__**\n\n𝒀𝒐𝒖❜𝒗𝒆 𝒆𝒏𝒂𝒃𝒍𝒆𝒅 𝒕𝒉𝒆 `𝙏𝙬𝙤-𝙎𝙩𝙚𝙥 𝙑𝙚𝙧𝙞𝙛𝙞𝙘𝙖𝙩𝙞𝙤𝙣` 𝒇𝒐𝒓 𝒚𝒐𝒖𝒓 𝒂𝒄𝒄𝒐𝒖𝒏𝒕.\n𝑷𝒍𝒆𝒂𝒔𝒆 𝒆𝒏𝒕𝒆𝒓 𝒚𝒐𝒖𝒓 `𝙏𝙬𝙤-𝙎𝙩𝙚𝙥 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙`\n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒑𝒓𝒆𝒔𝒔 /cancel 𝒊𝒇 𝒚𝒐𝒖 𝒅𝒐𝒏❜𝒕 𝒘𝒂𝒏𝒏𝒂 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔."""


@Ultron.on_message(filters.private & filters.command("start"))
async def string(_, msg: Message):
    if msg.chat.id in Var.BANNED:
        await Ultron.send_message(
            chat_id=msg.chat.id,
            text="𝑺𝒐𝒓𝒓𝒚, 𝑩𝒖𝒕 𝒂𝒄𝒄𝒐𝒓𝒅𝒊𝒏𝒈 𝒕𝒐 𝒎𝒆 𝒚𝒐𝒖❜𝒓𝒆 𝑩𝒂𝒏𝒏𝒆𝒅.\n𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒎𝒚 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 𝒇𝒐𝒓 𝒎𝒐𝒓𝒆 𝑰𝒏𝒇𝒐.",
            reply_to_message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup
            (
                [
                    [
                        InlineKeyboardButton
                        (
                            "🔱 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 🔱", url=f"https://t.me/{group}"
                        )
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return
    
    if support:
        try:
            user = await Ultron.get_chat_member(support, msg.chat.id)
            if user.status == "kicked":
                await Ultron.send_message(
                    chat_id=msg.chat.id,
                    text="𝑺𝒐𝒓𝒓𝒚, 𝑩𝒖𝒕 𝒂𝒄𝒄𝒐𝒓𝒅𝒊𝒏𝒈 𝒕𝒐 𝒎𝒆 𝒚𝒐𝒖❜𝒓𝒆 𝑩𝒂𝒏𝒏𝒆𝒅.\n𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒎𝒚 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 𝒇𝒐𝒓 𝒎𝒐𝒓𝒆 𝑰𝒏𝒇𝒐.",
                    reply_to_message_id=msg.message_id,
                    reply_markup=InlineKeyboardMarkup
                    (
                        [
                            [
                                InlineKeyboardButton
                                (
                                    "🔱 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 🔱", url=f"https://t.me/{group}"
                                )
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
        except UserNotParticipant:
            await Ultron.send_message(
                chat_id=msg.chat.id,
                text="**𝒀𝒐𝒖❜𝒗𝒆 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒎𝒚 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒊𝒏 𝒐𝒓𝒅𝒆𝒓 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆.**",
                reply_to_message_id=msg.message_id,
                reply_markup=InlineKeyboardMarkup
                (
                    [
                        [
                            InlineKeyboardButton
                            (
                                "⚜️ Jᴏɪɴ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ ⚜️", url=f"https://t.me/{support}"
                            )
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await Ultron.send_message(
                chat_id=msg.chat.id,
                text="**𝙎𝙊𝙈𝙀𝙏𝙃𝙄𝙉𝙂 𝙒3𝙉𝙏 𝙒𝙍𝙊𝙉𝙂 !!\n𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒎𝒚 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 𝒇𝒐𝒓 𝒎𝒐𝒓𝒆 𝑰𝒏𝒇𝒐.**",
                reply_to_message_id=msg.message_id,
                reply_markup=InlineKeyboardMarkup
                (
                    [
                        [
                            InlineKeyboardButton
                            (
                                "🔱 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 🔱", url=f"https://t.me/{group}"
                            )
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
    
    chat = msg.chat
    
    # Getting API_ID
    api = await Ultron.ask(
        chat.id, GREETING.format(msg.from_user.mention), disable_web_page_preview=True,
    )
    if await is_cancel(msg, api.text):
        return
    try:
        # Checking API_ID
        check_api = int(api.text)
    except Exception:
        await msg.reply("`𝘼𝙋𝙄_𝙄𝘿` 𝒊𝒔 𝑰𝒏𝒗𝒂𝒍𝒊𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    # Storing API_ID for Session
    api_id = api.text
    
    # Getting API_HASH 
    hash = await Ultron.ask(
        chat.id, HASH, disable_web_page_preview=True
    )
    if await is_cancel(msg, hash.text):
        return
    # Checking API_HASH
    if not len(hash.text) >= 30:
        await msg.reply("`𝘼𝙋𝙄_𝙃𝘼𝙎𝙃` 𝒊𝒔 𝑰𝒏𝒗𝒂𝒍𝒊𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    # Storing API_HASH for Session
    api_hash = hash.text
    # If API_HASH is Valid
    while True:
        # Getting Phone Number
        number = await Ultron.ask(
            chat.id, NUMBER
        )
        if not number.text:
            continue
        if await is_cancel(msg, number.text):
            return
        phone = number.text
        # Confirming if provided Number is Correct
        confirm = await Ultron.ask(
            chat.id, CONFIRMATION
        )
        if await is_cancel(msg, confirm.text):
            return
        if "y" in confirm.text:
            break
    try:
        session = Ultron("Ultron_PyroSession", api_id=api_id, api_hash=api_hash)
    try:
        await session.connect()
    except ConnectionError:
        await session.disconnect()
        await session.connect()
    try:
        code = await session.send_code(phone)
        await asyncio.sleep(1)
    except FloodWait as e:
        await msg.reply(f"𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒘𝒂𝒊𝒕, 𝒂𝒔 𝒚𝒐𝒖 𝒈𝒐𝒕 𝒂 𝑭𝒍𝒐𝒐𝒅𝑾𝒂𝒊𝒕 𝒐𝒇 {e.x} 𝑺𝒆𝒄𝒐𝒏𝒅𝒔 !!")
        return
    except ApiIdInvalid:
        await msg.reply("`𝘼𝙋𝙄_𝙄𝘿` 𝒂𝒏𝒅 `𝘼𝙋𝙄_𝙃𝘼𝙎𝙃` 𝒂𝒓𝒆 𝑰𝒏𝒗𝒂𝒍𝒊𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    except PhoneNumberInvalid:
        await msg.reply("𝑻𝒉𝒆 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅 𝑷𝒉𝒐𝒏𝒆 𝑵𝒖𝒎𝒃𝒆𝒓 𝒊𝒔 𝑰𝒏𝒗𝒂𝒍𝒊𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    try:
        otp = await Ultron.ask(
            chat.id, OTP, timeout=300
        )
    except TimeoutError:
        await msg.reply("𝑺𝒐𝒓𝒓𝒚, 𝒀𝒐𝒖❜𝒗𝒆 𝒓𝒆𝒂𝒄𝒉𝒆𝒅 𝒕𝒉𝒆 𝑻𝒊𝒎𝒆 𝑳𝒊𝒎𝒊𝒕 𝒐𝒇 5 𝒎𝒊𝒏𝒖𝒕𝒆𝒔.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    if await is_cancel(msg, otp.text):
        return
    otp_code = otp.text
    try:
        await session.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except PhoneCodeInvalid:
        await msg.reply("𝑰𝒏𝒗𝒂𝒍𝒊𝒅 𝑶𝑻𝑷 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    except PhoneCodeExpired:
        await msg.reply("𝑻𝒉𝒆 𝑶𝑻𝑷 𝒄𝒐𝒅𝒆 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒆𝒙𝒑𝒊𝒓𝒆𝒅.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await Ultron.ask(
                chat.id, TWO_STEP_VERIFICATION, timeout=300
            )
        except TimeoutError:
            await msg.reply("𝑺𝒐𝒓𝒓𝒚, 𝒀𝒐𝒖❜𝒗𝒆 𝒓𝒆𝒂𝒄𝒉𝒆𝒅 𝒕𝒉𝒆 𝑻𝒊𝒎𝒆 𝑳𝒊𝒎𝒊𝒕 𝒐𝒇 5 𝒎𝒊𝒏𝒖𝒕𝒆𝒔.\n𝑷𝒓𝒆𝒔𝒔 /start 𝒕𝒐 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏.")
            return
        if await is_cancel(msg, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await session.check_password(new_code)
        except Exception as e:
            await msg.reply(f"**𝙀𝙍𝙍𝙊𝙍 :** `{str(e)}`")
            return
    except Exception as e:
        await Ultron.send_message(chat.id, f"**𝙀𝙍𝙍𝙊𝙍 :** `{str(e)}`")
        return
    try:
        pyro_session =  await session.export_session_string()
        await session.send_message("me", f"""**👇 𝑯𝒆𝒓𝒆 𝒊𝒔 𝒚𝒐𝒖𝒓 𝑷𝒚𝒓𝒐𝑮𝒓𝒂𝒎 𝑺𝒕𝒓𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 👇**\n𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒆𝒅 𝒖𝒔𝒊𝒏𝒈 [{bot}](https://t.me/{bot_name})\n\n```{pyro_session}```\n\n**👆 𝑻𝒂𝒑 𝒕𝒐 𝑪𝒐𝒑𝒚 👆**\n#PyroGram #Session #Ultron""", disable_web_page_preview=True)
        await session.disconnect()
        text = "𝒀𝒐𝒖𝒓 𝑷𝒚𝒓𝒐𝑮𝒓𝒂𝒎 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒘𝒂𝒔 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒆𝒅 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚.✅\n𝑻𝒂𝒑 𝑩𝒆𝒍𝒐𝒘 𝒕𝒐 𝒈𝒆𝒕 𝒊𝒕.👇"
        reply_markup = InlineKeyboardMarkup
        (
            [
                [
                    InlineKeyboardButton
                    (
                        "😼 Gᴇᴛ Sᴛʀɪɴɢ Sᴇssɪᴏɴ 😼", url=f"tg://openmessage?user_id={chat.id}"
                    )
                ]
            ]
        )
        await Ultron.send_message(chat.id, text, reply_markup=reply_markup)
    except Exception as e:
        await Ultron.send_message(chat.id, f"****𝙀𝙍𝙍𝙊𝙍 :** `{str(e)}`")
        return
    
@Ultron.on_message(filters.private & filters.command("restart"))
async def restart(_, msg: Message):
    if msg.from_user.id == 1732236209:
        await msg.reply("𝑹𝒆𝒔𝒕𝒂𝒓𝒕𝒆𝒅 𝒕𝒉𝒆 𝑩𝒐𝒕 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚❗❗")
        return Var.HEROKU_APP.restart()
    
@Ultron.on_message(filters.private & filters.command("help"))
async def help(_, msg: Message):
    help_text = f"""
**𝑯𝒊!! {msg.from_user.mention}**\n𝑰❜𝒎 **PʏʀᴏGʀᴀᴍ Sᴛʀɪɴɢ Sᴇssɪᴏɴ Gᴇɴᴇʀᴀᴛᴏʀ**\n\n𝑰 𝒄𝒂𝒏 𝒉𝒆𝒍𝒑 𝒚𝒐𝒖 𝒕𝒐 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒆 𝒂 𝑷𝒚𝒓𝒐𝑮𝒓𝒂𝒎 𝑺𝒕𝒓𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒇𝒐𝒓 𝒚𝒐𝒖𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑨𝒄𝒄𝒐𝒖𝒏𝒕 𝒊𝒏 𝒂𝒏 𝑬𝒂𝒔𝒚 𝑾𝒂𝒚... \n
- 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒐𝒏 𝒓𝒆𝒒𝒖𝒊𝒓𝒆𝒔 𝒚𝒐𝒖𝒓 `𝘼𝙋𝙄_𝙄𝘿`, `𝘼𝙋𝙄_𝙃𝘼𝙎𝙃`, `𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧 𝙤𝙛 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘼𝙘𝙘𝙤𝙪𝙣𝙩`, `𝙊𝙏𝙋`, 𝒂𝒏𝒅 `𝙏𝙬𝙤-𝙎𝙩𝙚𝙥 𝙑𝙚𝙧𝙞𝙛𝙞𝙘𝙖𝙩𝙞𝙤𝙣 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙` (ɪғ ᴀɴʏ). \n
- `𝙊𝙏𝙋` 𝒘𝒊𝒍𝒍 𝒃𝒆 𝒔𝒆𝒏𝒕 𝒕𝒐 𝒚𝒐𝒖 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒚𝒐𝒖𝒓 𝑴𝒐𝒃𝒊𝒍𝒆 𝑷𝒉𝒐𝒏𝒆 𝒐𝒓 𝒗𝒊𝒂 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑨𝒑𝒑. \
𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒆𝒏𝒕𝒆𝒓 𝒕𝒉𝒆 `𝙊𝙏𝙋` 𝒊𝒏 𝒕𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒇𝒐𝒓𝒎𝒂𝒕 :~ `1 2 3 4 5` __(𝙎𝙥𝙖𝙘𝙚 𝙗𝙚𝙩𝙬𝙚𝙚𝙣 𝙚𝙖𝙘𝙝 𝙣𝙪𝙢𝙗𝙚𝙧.)__ \n
- 𝑰𝒇 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆𝒏❜𝒕 𝒓𝒆𝒄𝒆𝒊𝒗𝒆𝒅 𝒂𝒏𝒚 `𝙊𝙏𝙋`, 𝒕𝒉𝒆𝒏 𝒕𝒓𝒚 𝒂𝒏𝒅 𝑮𝒐-𝑨𝒉𝒆𝒂𝒅 𝒔𝒕𝒂𝒓𝒕𝒊𝒏𝒈 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒂𝒈𝒂𝒊𝒏 𝒘𝒊𝒕𝒉 /start 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 \n\n
**Nᴏᴛᴇ :~ 𝒀𝒐𝒖 𝒎𝒖𝒔𝒕 𝒏𝒆𝒆𝒅 𝒕𝒐 𝑱𝒐𝒊𝒏 𝒕𝒉𝒆 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒇𝒐𝒓 𝒕𝒉𝒊𝒔 𝑩𝒐𝒕 𝒊𝒏 𝒐𝒓𝒅𝒆𝒓 𝒕𝒐 𝒖𝒔𝒆 𝒊𝒕.**
"""
    chat = msg.chat
    await Ultron.send_message(
        chat_id=chat.id,
        text=help_text,
        reply_to_message_id=msg.message_id,
        reply_markup=InlineKeyboardMarkup
        (
            [
                [
                    InlineKeyboardButton
                    (
                        "⚜️ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ ⚜️", url=f"https://t.me/{support}"
                    ),
                    InlineKeyboardButton
                    (
                        "🔱 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 🔱", url=f"https://t.me/{group}"
                    )
                ],
                [
                    InlineKeyboardButton
                    (
                        "🔰 Oᴡɴᴇʀ 🔰", url=f"https://t.me/{owner}"
                    ),
                    InlineKeyboardButton
                    (
                        "💠 DEV 💠", url=f"https://t.me/{dev}"
                    )
                ]
            ]
        )
    )
    
async def is_cancel(msg: Message, text: str):
    if text.startswith("/cancel"):
        chat = msg.chat
        await Ultron.send_message(
            chat_id=chat.id,
            text="𝑷𝒓𝒐𝒄𝒆𝒔𝒔 𝑪𝒂𝒏𝒄𝒆𝒍𝒍𝒆𝒅 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚",
            reply_to_message_id=msg.message_id
        )
        return True
    return False

if __name__ == "__main__":
    Ultron.run()
