import os
import logging
import logging.config

logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyromod import listen
from pyrogram import Client as Ultron
from heroku3 import from_key

TOKEN = os.environ.get("TOKEN", None)
APP_NAME = os.environ.get("NAME", None)
HEROKU_API = os.environ.get("API", None)
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)

HU_APP = from_key(HEROKU_API).apps()[APP_NAME]

def main():
    plugins = dict(root="session")
    app = Ultron("PyroSession",
                 bot_token=TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)
    app.run()
    
if __name__ == "__main__":
    main()
