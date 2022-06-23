## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgA6G4m4gAEZp_AHAeBUIKHiQlrwNjr32cyyJKFw0lyxMUrD9lAkKp62WiWkApOJ2eKQ-ZoNS1Fpz6FcmDb_tqvmDzQ8QdnSH-KFWBea8byMaOBeuZRPkMu_qZki4O3h7J6nKgwz3v4VVFFvfjGH5nsXFlqdZNeyGEC7fjDDn1ITT0WD6y45D3gzBoeh8WYKD13d6a8RrdYddY7olIO-BuG-D1Ev24VoTeFJJP_33xRZZO92Xqut7h5p53ubKl8g9XcqzqHW4GRq2TNuYgkCDl3rDowjbRJxEOGTJoMs5B3ap1BvS13FDgGd2NyLPbUMiS4_ZR2x69ndP9KEYNzCeKqAbcfRewA")
BOT_TOKEN = getenv("BOT_TOKEN", "5310747101:AAERlg5g4Yv6uqHNNV0MBUM4solUSn6KFAg")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "qvvql")
ALIVE_NAME = getenv("ALIVE_NAME", "peter")
BOT_USERNAME = getenv("BOT_USERNAME", "musicathenabot")
OWNER_ID = getenv("OWNER_ID", "1769740278")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "svvsl")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "qvvqlIl")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "qvvqIII")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1769740278").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
