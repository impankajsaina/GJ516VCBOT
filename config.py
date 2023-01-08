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
SESSION_NAME = getenv("SESSION_NAME", "BQC_SMpIkX3-DCln8URSk5hAit0-_DYxTDGhaR2_IgmUeB9KrsCdMXUaBS1d5QiHZKnPQDEUoD_q-KlPTte4v-wgMTQnRaqRmFtjfI0tMDWAmB-pUErihJ4gbgVP95Hxlp-KsV0I7hueWn3GKLJlHojj3e5sGfAAh3t2BEB4ywP4XpPIIzgvSyewELWdE4d4MAp1irMH-9piHHjM0n-mkgbFyCPJlwDvBldEY-_iYBzO-Tf36YhJaoy9sus4ceyddrq9gjNluLI3cL0BhnBkSEbq066YmOqBHnMRUGubCYKPlMKBPsIBoV0IW1b2J0iT2G8-_eUvu3aG5Y16vSh9zJ0AazqD4wA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1353235020").split()))
