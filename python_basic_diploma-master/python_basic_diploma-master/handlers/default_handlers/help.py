from telebot.types import Message
from loader import bot
from states.user_states import UserState


@bot.callback_query_handler(func=lambda call: call.data == 'help_command', state=UserState.chat_started)
def help_callback(call):
    help_cmd(call)


@bot.message_handler(commands=['help'], state=UserState.chat_started)
def help_cmd(message: Message):
    bot.send_message(message.from_user.id, 'Список команд:\n<b>/start</b> - начало работы с ботом'
                                      '\n<b>/help</b> - вывод списка доступных команд'
                                      '\n<b>/low</b> - вывод минимальных показателей'
                                      '\n<b>/high</b> - вывод максимальных показателей'
                                      '\n<b>/custom</b> - вывод показателей пользовательского диапазона'
                                      '\n<b>/history</b> - вывод истории запросов', parse_mode='html')