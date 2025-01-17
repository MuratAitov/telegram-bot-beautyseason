from pathlib import Path
from aiogram import Bot
from aiogram.types import FSInputFile

class FileManager:
    def __init__(self):
        # Путь к папке с файлами гайдов
        self.guides_path = Path(__file__).parent.parent / "files" / "guides"
        self.guides_path.mkdir(parents=True, exist_ok=True)

    async def send_acne_guide(self, bot: Bot, chat_id: int) -> None:
        """Отправка гайда по акне"""
        file_path = self.guides_path / "acne_guide.pdf"
        guide = FSInputFile(file_path)
        await bot.send_document(
            chat_id=chat_id,
            document=guide,
            caption="Ваш гайд по лечению акне. Спасибо за подписку!"
        )

    async def send_pigmentation_guide(self, bot: Bot, chat_id: int) -> None:
        """Отправка гайда по пигментации"""
        file_path = self.guides_path / "pigmentation_guide.pdf"
        guide = FSInputFile(file_path)
        await bot.send_document(
            chat_id=chat_id,
            document=guide,
            caption="Ваш гайд по лечению пигментации. Спасибо за подписку!"
        )