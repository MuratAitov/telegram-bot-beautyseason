from aiogram import Bot
from aiogram.enums import ChatMemberStatus

async def check_subscription(bot: Bot, user_id: int, channel_id: str = "@beauty_season_kzn") -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.CREATOR
        ]
    except Exception as e:
        print(f"Ошибка при проверке подписки: {e}")
        return False