from telebot import TeleBot
from settings import project_settings


class CryptoTrackerBot:
    def __init__(self):
        self.token = project_settings.get("TG_BOT_TOKEN")
        if not self.token:
            raise Exception("Failed to get TG_BOT_TOKEN from settings")
        self.bot = TeleBot(self.token)
        self.recipients = project_settings.get("MESSAGES_RECIPIENTS")

    def send_message(self, message_text):
        for recipient_id in self.recipients:
            self.bot.send_message(
                chat_id=recipient_id,
                text=message_text
            )
