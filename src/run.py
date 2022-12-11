import logging

from telegram import CryptoTrackerBot
from trackers import CryptorankCoinTracker
from settings import project_settings


def main():
    bot = CryptoTrackerBot()
    tracker = CryptorankCoinTracker()

    message_text = tracker.compare_prices()
    bot.send_message(message_text)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(e)
