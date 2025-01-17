from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

def get_main_keyboard():
    keyboard = [
        [
            KeyboardButton(text="Перейти в Telegram-канал"),
            KeyboardButton(text="Записаться на процедуру")
        ],
        [KeyboardButton(text="Гайд по лечению акне")],
        [KeyboardButton(text="Гайд по лечению пигментации")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это красивый бот клиник эстетической медицины Beauty Season! "
        "Выберите, что вас интересует",
        reply_markup=get_main_keyboard()
    )