import time
import os
from dotenv import load_dotenv
import requests

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_alert(message):
    requests.post(WEBHOOK_URL, json={"content": message})