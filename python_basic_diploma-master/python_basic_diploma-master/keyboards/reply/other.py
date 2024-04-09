from telebot import types


other_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
other_markup.add(types.KeyboardButton('/help', ))
