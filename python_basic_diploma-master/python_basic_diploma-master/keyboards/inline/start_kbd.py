from telebot import types

start_markup = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='Список доступных действий',
                                  callback_data='help_command')
btn2 = types.InlineKeyboardButton(text='Вывод минимальных показателей',
                                  callback_data='low_command')
btn3 = types.InlineKeyboardButton(text='Вывод максимальных показателей',
                                  callback_data='high_command')
btn4 = types.InlineKeyboardButton(text='Вывод показателей пользовательского диапазона',
                                  callback_data='custom_command')
btn5 = types.InlineKeyboardButton(text='Вывод истории запросов',
                                  callback_data='history_command')
start_markup.row(btn2)
start_markup.row(btn3)
start_markup.row(btn4)
start_markup.row(btn5)