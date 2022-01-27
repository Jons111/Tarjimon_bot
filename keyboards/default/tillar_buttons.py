from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


tillar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Eng-Uz'),
            KeyboardButton(text='Rus-Uz')
        ],
        [
            KeyboardButton(text='Eng-Rus'),
            KeyboardButton(text='Kontakt',request_contact=True),
            KeyboardButton(text='Location',request_location=True),
        ]
    ],
    resize_keyboard=True
)