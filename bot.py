from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK = os.getenv("DISCORD_CHANNEL_ID")
SOLANA_WSOL_ADD = os.getenv("SOLANA_WSOL_ADD")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

print("Webhook URL:", WEBHOOK)
print("SOLANA_WSOL_ADD:", SOLANA_WSOL_ADD)
print("DISCORD_BOT_TOKEN:", DISCORD_BOT_TOKEN)
