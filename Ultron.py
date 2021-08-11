import os
import logging
import logging.config

logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyromod import listen
from heroku3 import from_key
from pyrogram import Client as Ultron
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

def main():
    plugins = dict(root="session")
    app = Ultron("PyroSession",
                 bot_token=Var.TOKEN,
                 api_id=Var.API_ID,
                 api_hash=Var.API_HASH,
                 plugins=plugins,
                 workers=100)
    app.run()
    
if __name__ == "__main__":
    main()
