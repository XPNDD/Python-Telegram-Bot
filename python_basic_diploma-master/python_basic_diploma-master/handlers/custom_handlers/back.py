from telebot.types import Message
from loader import bot
from states.user_states import UserState
from handlers.default_handlers import help


@bot.message_handler(commands=['back'], state=UserState.low_category_picking)
@bot.message_handler(commands=['back'], state=UserState.low_amount_picking)
@bot.message_handler(commands=['back'], state=UserState.high_category_picking)
@bot.message_handler(commands=['back'], state=UserState.high_amount_picking)
@bot.message_handler(commands=['back'], state=UserState.custom_category_picking)
@bot.message_handler(commands=['back'], state=UserState.custom_amount_picking)
@bot.message_handler(commands=['back'], state=UserState.bottom_border_picking)
@bot.message_handler(commands=['back'], state=UserState.upper_border_picking)
@bot.message_handler(commands=['back'], state=UserState.borders_set)
def back_cmd(message: Message):
    bot.set_state(message.from_user.id, UserState.chat_started)
    help.help_cmd(message)


@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.low_category_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.low_amount_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.high_category_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.high_amount_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.custom_category_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.custom_amount_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.bottom_border_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.upper_border_picking)
@bot.callback_query_handler(func=lambda call: call.data == 'back_command', state=UserState.borders_set)
def back_callback(call):
    back_cmd(call)
