from telebot.types import Message
from loader import bot
from keyboards.reply import categories
from states.user_states import UserState
from keyboards.inline import back_kbd
from utils.misc import categories_request, items_request

categories_lst = categories_request.cat_req()


@bot.callback_query_handler(func=lambda call: call.data == 'custom_command', state=UserState.chat_started)
def custom_callback(call):
    custom_cmd(call)


@bot.message_handler(commands=['custom'], state=UserState.chat_started)
def custom_cmd(message: Message):
    markup = categories.categories_markup
    categories_str = ''
    for category in categories_lst:
        categories_str += '\n' + '-' + category
    bot.send_message(message.from_user.id, f'Выберите категорию товаров, по которой будет производиться запрос:'
                                           f' <b>{categories_str}</b>', parse_mode='html', reply_markup=markup)
    bot.set_state(message.from_user.id, UserState.custom_category_picking)


@bot.message_handler(state=UserState.custom_category_picking)
def category_pick(message: Message):
    if message.text in categories_lst:
        bot.send_message(message.from_user.id, 'Сколько товаров из выбранной категории вы хотите получить? '
                                               '(введите число от 1 до 10)')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['category'] = message.text
        bot.set_state(message.from_user.id, UserState.custom_amount_picking)
    else:
        bot.send_message(message.from_user.id, 'Выберите 1 из доступных категорий.\n'
                                               'Чтобы отменить выбранную команду введите /back'
                                               ' или нажмите на кнопку',
                         reply_markup=back_kbd.back_markup)


@bot.message_handler(state=UserState.custom_amount_picking)
def pick_amount(message: Message):
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['amount'] = int(message.text)
        bot.send_message(message.from_user.id, 'Введите нижнюю границу выборки')
        bot.set_state(message.from_user.id, UserState.bottom_border_picking)
    else:
        bot.send_message(message.from_user.id, 'Введите число!\n'
                                               'Чтобы отменить выбранную команду введите /back '
                                               'или нажмите на кнопку',
                         reply_markup=back_kbd.back_markup)


@bot.message_handler(state=UserState.bottom_border_picking)
def set_bottom_border(message: Message):
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['bottom_border'] = int(message.text)
        bot.send_message(message.from_user.id, 'Введите верхнюю границу выборки')
        bot.set_state(message.from_user.id, UserState.upper_border_picking)
    else:
        bot.send_message(message.from_user.id,
                         'Введите число!\n'
                         'Чтобы отменить выбранную команду введите /back '
                         'или нажмите на кнопку',
                         reply_markup=back_kbd.back_markup)


@bot.message_handler(state=UserState.upper_border_picking)
def set_upper_border(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if message.text.isdigit():
            if int(message.text) > data['bottom_border']:
                data['upper_border'] = int(message.text)
                url = 'https://fakestoreapi.com/products/category/'
                url += data['category']
                items_lst = items_request.items_req(url)
                temp_items_lst = []
                for bordered_item in items_lst:
                    if data['bottom_border'] <= bordered_item['price'] <= data['upper_border']:
                        temp_items_lst.append(bordered_item)
                if len(temp_items_lst) > 0:
                    if data['amount'] > len(temp_items_lst):
                        temp_count = len(temp_items_lst)
                    else:
                        temp_count = data['amount']
                    bot.send_message(message.from_user.id,
                                     f'Товары из категории {data["category"]}:')
                    for piece in range(temp_count):
                        item_msg = ''
                        for key, value in temp_items_lst[piece].items():
                            item_msg += '\n' + str(key) + ': ' + str(value) + '\n'
                        bot.send_message(message.from_user.id, item_msg)
                    bot.set_state(message.from_user.id, UserState.chat_started)
                else:
                    bot.send_message(message.from_user.id, 'Товары из выбранной категории '
                                                           'в данном ценовом диапазоне '
                                                           'не найдены')
                items_lst.clear()
                temp_items_lst.clear()
            else:
                bot.send_message(message.from_user.id,
                                 'Верхняя граница должна быть больше нижней!'
                                 'Чтобы отменить выбранную команду введите /back '
                                 'или нажмите на кнопку',
                                 reply_markup=back_kbd.back_markup)
        else:
            bot.send_message(message.from_user.id,
                             'Введите число!\n'
                             'Чтобы отменить выбранную команду введите /back '
                             'или нажмите на кнопку',
                             reply_markup=back_kbd.back_markup)


