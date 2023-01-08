from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "26144852"))
API_HASH = getenv("API_HASH", "f437972ec6dd0bd5e34599d9e83ee9ad")
BOT_TOKEN = getenv("BOT_TOKEN", "5831028973:AAFVHD4asdU66UHon-pmNegB-EhQy63z8us")
BOT_NAME = getenv("BOT_NAME",""𝄟🦋⃟≛⃝🇦‌ꪜ𝙴Й₲𝙴ℝ𝚂🦋⃟ ♡︎乛ᴍᴜsɪᴄ)
BOT_USERNAME = getenv("BOT_USERNAME", "Fllanexm_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "HNYPROBOY")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FRIENDZVIBES")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "RoY_CREATIION")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/544ffbb6532ab48738625.jpg")
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzcBuzN9CoMiHYFL7NX58biutPpgMcm9_O4RXk2UMZMh7-DOM9A7NUipjtnemm5q7RU5_G0y-VtLFqUWLaMhz-vbc7juI5Awu-vTlgq-8T1RuEGe1Jxbw78vka0P4IgaZ96W5n_4ZCIxxrnJMthA0B6JhoLb2c3AFsnIpGROc6IF5QB4k_xCChqE3Ohf4ryMGD0Hxuvjpqf6VYp1nY9AbEtnZah3ls1ANYg9mmpXDhImvH5jO9o6aKkC6d-d0I6_Wuc0MfqjmWxY_aKpxp1LIitGGZ8P3jjZ65kTJv-XnbgOZUNJjYbOxcJrpQGnIpsKVKW1qydemlaqXyvyFyN4GGYkiJo=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5789556750").split()))
