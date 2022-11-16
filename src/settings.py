import os
import logging

from dotenv import load_dotenv


load_dotenv()

project_settings = {
    "TG_BOT_TOKEN": os.getenv("TG_BOT_TOKEN", None),
    "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
    "MESSAGES_RECIPIENTS": [
        recipient for recipient in os.getenv("MESSAGES_RECIPIENTS", "").split(",") if recipient
    ],
}

logging.basicConfig(
    level=project_settings["LOG_LEVEL"],
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s"
)
