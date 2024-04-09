from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    chat_started = State()

    low_category_picking = State()
    low_amount_picking = State()

    high_category_picking = State()
    high_amount_picking = State()

    custom_category_picking = State()
    custom_amount_picking = State()
    bottom_border_picking = State()
    upper_border_picking = State()
    borders_set = State()
