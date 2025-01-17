from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "Перейти в Telegram-канал")
async def channel_link(message: Message):
    await message.answer("Переходите по ссылке:\nhttps://t.me/beauty_season_kzn")

@router.message(F.text == "Записаться на процедуру")
async def book_procedure(message: Message):
    await message.answer("Переход по ссылке @Beauty_season_clinic")