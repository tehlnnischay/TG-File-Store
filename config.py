import os

API_ID = int(os.environ.get("API_ID", "20102429"))
API_HASH = os.environ.get("API_HASH", "0e9e788b4221aafb24c0c2603986333b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6526158665:AAEw4C-A1R-wzsD01lgtP_lIuXAKp5YZ9WE")
DB_CHANNEL_ID = os.environ.get("-1002021154583")
IS_PRIVATE = os.environ.get("IS_PRIVATE",True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get ("6842904149"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1002170133192')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split("6820525129 5146039165")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(6842904149)
