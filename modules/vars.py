#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23897874"))
API_HASH = environ.get("API_HASH", "ec91dd01da9693911a6ee4af5d0bef2c")
BOT_TOKEN = environ.get("BOT_TOKEN", "7696404581:AAF2rWbqYs4mhyp5EZGXks2LbCOlFLntVdU")

OWNER = int(environ.get("OWNER", "1572626591"))
CREDIT = environ.get("CREDIT", "@PROFE07XH")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1504965760').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7295124217').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



