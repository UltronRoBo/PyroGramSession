import os
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())


class Credentials:
    TOKEN = os.environ.get("TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BANNED = set(int(x) for x in os.environ.get("BANNED","1883752632 1698803654 1781874715 1712612576 1815892895 1622398047 1669570166").split())
