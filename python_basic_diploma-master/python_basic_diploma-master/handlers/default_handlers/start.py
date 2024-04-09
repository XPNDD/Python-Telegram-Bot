from telebot.types import Message
from loader import bot
from keyboards.inline import start_kbd
from states.user_states import UserState


@bot.message_handler(commands=['start'])
def start_cmd(message: Message):
    bot.set_state(message.from_user.id, UserState.chat_started)
    markup = start_kbd.start_markup
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)
