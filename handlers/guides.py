from aiogram import Router, F, Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.files import FileManager
from utils.subscription import check_subscription
from aiogram import types

router = Router()
file_manager = FileManager()

def get_subscription_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Подписаться на канал",
                    url="https://t.me/beauty_season_kzn"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Проверить подписку",
                    callback_data="check_subscription"
                )
            ]
        ]
    )
    return keyboard

@router.message(F.text == "Гайд по лечению акне")
async def acne_guide(message: Message, bot: Bot):
    is_subscribed = await check_subscription(bot, message.from_user.id)

    if not is_subscribed:
        await message.answer(
            "Для получения гайда необходимо подписаться на наш канал:",
            reply_markup=get_subscription_keyboard()
        )
        return

    await file_manager.send_acne_guide(bot, message.chat.id)
    await message.answer(
        "Ждем вас в наших клиниках по адресам в Казани:\n"
        "ул. Спартаковская, 2, корп. 1"
        "пр. Ибрагимова, 54\n"
        "ул. Сибгата Хакима, 42\n"

    )

@router.message(F.text == "Гайд по лечению пигментации")
async def pigmentation_guide(message: Message, bot: Bot):
    is_subscribed = await check_subscription(bot, message.from_user.id)

    if not is_subscribed:
        await message.answer(
            "Для получения гайда необходимо подписаться на наш канал:",
            reply_markup=get_subscription_keyboard()
        )
        return

    await file_manager.send_pigmentation_guide(bot, message.chat.id)
    await message.answer(
        "Ждем вас в наших клиниках по адресам в Казани:\n"
        "ул. Спартаковская, 2, корп. 1"
        "пр. Ибрагимова, 54\n"
        "ул. Сибгата Хакима, 42"
    )

@router.callback_query(F.data == "check_subscription")
async def check_sub_callback(callback: types.CallbackQuery, bot: Bot):
    is_subscribed = await check_subscription(bot, callback.from_user.id)

    if is_subscribed:
        await callback.message.answer("Спасибо за подписку! Отправляю гайд...")
        if "акне" in callback.message.text.lower():
            await file_manager.send_acne_guide(bot, callback.message.chat.id)
        else:
            await file_manager.send_pigmentation_guide(bot, callback.message.chat.id)
    else:
        await callback.answer("Вы еще не подписались на канал!", show_alert=True)

    await callback.answer()