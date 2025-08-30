from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

registration = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Registration')],
    ]
)

main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Блюда'),KeyboardButton(text='Завтраки')],
        [KeyboardButton(text='Напитки'),KeyboardButton(text='Сладости')]
    ]
)

admin_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Реклама'),KeyboardButton(text='Пользователи')]
    ]


)

