from __future__ import annotations

import telebot

from config import API_TOKEN, AUTHORS, INFO_IMAGE
from locales import locales


def process(bot: telebot.Telebots) -> None:
    """Функционал бота"""
    @bot.message_handler(commands=['start'])
    def start(message) -> None:
        """Запуска бота"""
        bot.send_message(message.chat.id, locales["welcome"])
        for author in AUTHORS:
            bot.send_message(message.chat.id, author)

    @bot.message_handler(commands=['info'])
    def info(message):
        """Информация"""
        bot.send_photo(message.chat.id, open(INFO_IMAGE, 'rb'), caption=locales["info"], parse_mode="html")

    @bot.message_handler(commands=['stop'])
    def stop(message):
        """Остановка бота"""
        bot.send_message(message.chat.id, locales["stop"])
        bot.stop_bot()


if __name__ == "__main__":
    bot: telebot.Telebot = telebot.TeleBot(API_TOKEN)
    process(bot)
    bot.infinity_polling()
