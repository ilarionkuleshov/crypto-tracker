import os
import logging

from dotenv import load_dotenv


load_dotenv()

project_settings = {
    "TG_BOT_TOKEN": os.getenv("TG_BOT_TOKEN", None),
    "CRYPTORANK_TOKEN": os.getenv("CRYPTORANK_TOKEN", None),
    "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
    "MESSAGES_RECIPIENTS": [
        recipient for recipient in os.getenv("MESSAGES_RECIPIENTS", "").split(",") if recipient
    ],
    "COIN_ID": int(os.getenv("COIN_ID", 0)),
    "STARTING_COIN_BALANCE": float(os.getenv("STARTING_COIN_BALANCE", 0)),
    "STARTING_PRICE_USD": float(os.getenv("STARTING_PRICE_USD", 0)),
}

logging.basicConfig(
    level=project_settings["LOG_LEVEL"],
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s"
)
