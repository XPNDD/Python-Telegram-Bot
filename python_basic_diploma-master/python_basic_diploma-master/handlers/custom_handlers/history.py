from telebot.types import Message
from loader import bot
from states.user_states import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'history_command', state=UserState.chat_started)
def custom_cmd(call):
    bot.send_message(call.message.chat.id, 'История запросов пользователя...')


@bot.message_handler(commands=['history'], state=UserState.chat_started)
def custom_cmd(message: Message):
    bot.send_message(message.chat.id, 'История запросов пользователя...')
