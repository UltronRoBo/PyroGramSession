import os

from pyromod import listen
from heroku3 import from_key
from pyrogram import Client
from typing import Dict, Optional, List
from pyrogram.errors import MessageNotModified

class Var:
    TOKEN = os.environ.get("TOKEN", None)
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", None)
    APP_NAME = os.environ.get("APP_NAME", None)
    HEROKU_API = os.environ.get("HEROKU_API", None)
    HEROKU_APP = from_key(HEROKU_API).apps()[APP_NAME]
    SUPPORT = os.environ.get("SUPPORT", "UltronSupport")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "UltronSupportChat")
    BANNED = set(int(x) for x in os.environ.get("BANNED","1883752632 1698803654 1781874715 1712612576 1815892895 1622398047 1669570166").split())

Ultron = Client(":memory:",
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=Var.TOKEN)
