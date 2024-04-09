from telebot import types

back_markup = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='/back', callback_data='back_command')
back_markup.add(btn)