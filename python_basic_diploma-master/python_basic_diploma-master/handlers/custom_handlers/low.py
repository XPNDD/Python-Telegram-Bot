from telebot.types import Message
from loader import bot
from keyboards.reply import categories
from states.user_states import UserState
from keyboards.inline import back_kbd
from utils.misc import categories_request, items_request


categories_lst = categories_request.cat_req()


@bot.callback_query_handler(func=lambda call: call.data == 'low_command', state=UserState.chat_started)
def low_callback(call):
    low_cmd(call)


@bot.message_handler(commands=['low'], state=UserState.chat_started)
def low_cmd(message: Message):
    markup = categories.categories_markup
    categories_str = ''
    for category in categories_lst:
        categories_str += '\n' + '-' + category
    bot.send_message(message.from_user.id, f'Выберите категорию товаров, по которой будет производиться запрос:'
                                           f' <b>{categories_str}</b>', parse_mode='html', reply_markup=markup)
    bot.set_state(message.from_user.id, UserState.low_category_picking)


@bot.message_handler(state=UserState.low_category_picking)
def category_pick(message: Message):
    if message.text in categories_lst:
        bot.send_message(message.from_user.id, 'Сколько товаров из выбранной категории вы хотите получить? '
                                               '(введите число от 1 до 10)')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['category'] = message.text
        bot.set_state(message.from_user.id, UserState.low_amount_picking)
    else:
        bot.send_message(message.from_user.id, 'Выберите 1 из доступных категорий.\n'
                                               'Чтобы отменить выбранную команду введите /back'
                                               ' или нажмите на кнопку',
                         reply_markup=back_kbd.back_markup)


@bot.message_handler(state=UserState.low_amount_picking)
def pick_amount(message: Message):
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['amount'] = int(message.text)
        url = 'https://fakestoreapi.com/products/category/'
        url += data['category']
        items_lst = items_request.items_req(url)
        temp_items_lst = sorted(items_lst, key=lambda dct: dct['price'])
        bot.send_message(message.from_user.id, f'Товары из категории {data["category"]}:')
        if data['amount'] > len(items_lst):
            data['amount'] = len(items_lst)
        for piece in range(data['amount']):
            item_msg = ''
            for key, value in temp_items_lst[piece].items():
                item_msg += '\n' + str(key) + ': ' + str(value) + '\n'
            bot.send_message(message.from_user.id, item_msg)
        items_lst.clear()
        bot.set_state(message.from_user.id, UserState.chat_started)
    else:
        bot.send_message(message.from_user.id, 'Введите число!\n'
                                               'Чтобы отменить выбранную команду введите /back '
                                               'или нажмите на кнопку',
                         reply_markup=back_kbd.back_markup)
