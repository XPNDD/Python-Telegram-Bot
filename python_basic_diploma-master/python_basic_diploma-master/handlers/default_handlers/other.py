from telebot.types import Message
from loader import bot
from keyboards.reply import other
from states.user_states import UserState


@bot.message_handler(state=UserState.chat_started)
def other_cmd(message: Message):
    markup = other.other_markup
    bot.reply_to(message, 'Команда не распознана')
    bot.send_message(message.chat.id, 'Для списка доступных действий используйте команду <b>/help</b>',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['document', 'audio', 'voice', 'photo',
                                    'location', 'contact', 'sticker', 'video_note'], state=UserState.chat_started)
def media_received(message: Message):
    markup = other.other_markup
    bot.reply_to(message, 'Я не могу воспринимать медиафайлы и т.п.')
    bot.send_message(message.chat.id, 'Для списка доступных действий используйте команду <b>/help</b>',
                     parse_mode='html', reply_markup=markup)
