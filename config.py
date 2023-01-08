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
OWNER_USERNAME = getenv("OWNER_USERNAME", "HNYPROBOY")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FRIENDZVIBES")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "RoY_CREATIION")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQCdowYAt-zlNOTXPaoPpLIAEV1m3iw-eM3eTA-735gB-srdsG7mBYGHiNPjXOlV_asS0dhggkA8ii-5PB9X8cBaipb3IP8xvF2wUFhhqUAu_0i3a3CDea_mEuUiO5GFlflQQrk1R_pH5kWvVUA-xb4TVkPXkV-8SiWKCpVP-BePjnfMhAAbyxE__vcskylgpd90sqDcub2J8Y9xald-JlpSkCEqg0yyfkdTSG_eXemJ1LEgxHiTCx-otA39Xm_a5vMsthRmkrdOwP6Q0e53bOc8wzeMLPy3RYG5MWALWIjEY8zwh0jn9o5LZ6tlNAbR5hSgSn19LY0G24WPIf9IAZttB7hbhAAAAABrOoPjAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5789556750").split()))
