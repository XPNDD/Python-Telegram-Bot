from telebot import types
from utils.misc import categories_request


temp = categories_request.cat_req()

categories_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
for item in temp:
    categories_markup.add(types.KeyboardButton(item))
