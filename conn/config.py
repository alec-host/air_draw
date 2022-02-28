from dotenv import load_dotenv

import os

load_dotenv()

MYSQL_USER    = os.getenv("MYSQL_USER")
MYSQL_PASS    = os.getenv("MYSQL_PASS")
MYSQL_URL     = os.getenv("MYSQL_URL")
MYSQL_DBASE   = os.getenv("MYSQL_DBASE")
REDIS_HOST    = os.getenv("REDIS_HOST")
REDIS_PORT    = os.getenv("REDIS_PORT")
REDIS_PASS    = os.getenv("REDIS_PASS")
ENTRIES_DIR   = os.getenv("ENTRIES_DIR")
CONNECT_DIR   = os.getenv("CONNECT_DIR")
UTILITY_DIR   = os.getenv("UTILITY_DIR")
DRAW_DIR      = os.getenv("DRAW_DIR")
REGISTER_DIR  = os.getenv("REGISTER_DIR")