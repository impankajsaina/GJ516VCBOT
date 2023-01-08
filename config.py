from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10330886"))
API_HASH = getenv("API_HASH", "8b88ae0d20e10c5b5c87f4d115fb6d7b")
BOT_TOKEN = getenv("BOT_TOKEN", "5301190359:AAHmawrPFwU5UftV_DBjtaO2ja7aepYRQBI")
BOT_NAME = getenv("BOT_NAME","𝄟🦋⃟≛⃝🇦‌ꪜ𝙴Й₲𝙴ℝ𝚂🦋⃟ ♡︎乛🇲‌🇺‌🇸‌🇮‌🇨‌")
BOT_USERNAME = getenv("BOT_USERNAME", "AMUSICROBOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FRIENDZVIBES")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "FRIENDZVIBES")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQCYYLDImvtNBCgo8VzcewbDEBmhnO3dEzwmnJOxUQEhH9Su4ObLqnX6s7ooZAFoApIBbCJiyIfmi7gIcmQxPrBOIH14h8hUpI76px0cFXZtyG4a9OFXLqXQQUAtooBQQ8_t0hn2S6OH9Ung4ux8JtWJrEdg88T76B3B98frABsdg79iWg1PjGBzxC1oGVpzp7L4q1aYNnkgh7l7sMsxSNMlMxkVaZB0fIb44U7tX41GIBuZ1KUriQoMD-xbFfpHh7-It58Xya9Z-bHRrPzYqpL9Njt6c6sxG4AW-NIHOpkTZ0EuTBsk2FvgTruMgJc-v8vGBESab9HBvBD9nDKN-BmeazqD4wA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1353235020").split()))
