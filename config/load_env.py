# config/load_env.py

from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "DISCORD_CHANNEL_ID": os.getenv("DISCORD_CHANNEL_ID"),
        "DISCORD_BOT_TOKEN": os.getenv("DISCORD_BOT_TOKEN"),
        "SOLANA_WSOL_ADD": os.getenv("SOLANA_WSOL_ADD"),
    }
