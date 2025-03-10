import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from googletrans import Translator

TOKEN = "7590369025:AAGwc_vspK7fCWyZmRxi4iqKRA_0g7c17bs"  # Thay token bot vào đây

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message()
async def auto_translate(message: Message):
    """Tự động dịch nếu phát hiện tin nhắn không phải tiếng Việt."""
    detected_lang = translator.detect(message.text).lang  # Nhận diện ngôn ngữ
    if detected_lang != "vi":  # Nếu không phải tiếng Việt thì dịch
        translated_text = translator.translate(message.text, dest="vi").text
        await message.reply(f"🔄 Dịch từ {detected_lang.upper()}:\n**{translated_text}**")

@dp.message(Command("dịch"))
async def manual_translate(message: Message):
    """Dịch thủ công khi dùng lệnh /dịch."""
    text = message.text.replace("/dịch", "").strip()
    if not text:
        await message.reply("⚠ Vui lòng nhập nội dung cần dịch!")
        return
    translated_text = translator.translate(text, dest="vi").text
    await message.reply(f"🔄 Dịch:\n**{translated_text}**")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())