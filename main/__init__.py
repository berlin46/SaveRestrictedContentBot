#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22275013
API_HASH = 3d907e836adcc5d05b821a8cc98d9f22
BOT_TOKEN = 5876760911:AAH94qCWZogwnd03KQ2C3Wu3Eo87ixfUR9o
SESSION = AQBGPf6menU2NGBrMSH_NhAyW_1SR_ZsDIRbdSxIEPXAVwWV-UBcmHsbUS3GQu0AuSxCK8FNtx9mHim-c69o9lIO0e0fsRSQyJPQOcHVPefcN7Z0rjvMG5m5ZQWDhSJHFl28ejGgFn3qcXwUdBYn9yruO4hQzOxdHxlfjctMxIESaAzsYF-fdLUS0v5uT4W0kTUj81AbtKnkOniZSP6T5aBXlJQpu5cDyg04jDV0ZCQ3Lc-pYZDqrJsypIsGk9xafAF3PC8AMo6l9ez27Rvle9r7iN0Z9Hecto53swnT-7WY5E5qX-deIa_QyDfmWwEk8gAfLw2OBNjKvnh9q-8OdfeyAAAAAVRMm1IA
FORCESUB = pineapplexyxx
AUTH = 5709273938

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
