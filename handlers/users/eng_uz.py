from aiogram import types
from googletrans import Translator
from loader import dp
tarjimon = Translator()

# Echo bot
@dp.message_handler(text='Eng-Uz')
async def bot_echo(message: types.Message):
    matn = message.text
    til = tarjimon.detect(message.text).lang

    await message.answer(text='english sozlarni kiriting uzga tarjima qilib beradi')
