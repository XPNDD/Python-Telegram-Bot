from telebot.types import Message
from loader import bot


@bot.message_handler()
def echo(message: Message):
    bot.reply_to(message, f'Сообщение: {message.text}')
