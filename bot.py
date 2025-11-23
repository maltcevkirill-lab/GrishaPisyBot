import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7636498052:AAH9M_7P8cW9eK8z9YcX7vB6nL5mK4jH3gF'
TARGET_USER_ID = 532562432                      # ← ID того, на кого реагируем
VIDEO_FILES = ['pisy.mp4']

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def send_video(message: types.Message):
    if message.from_user and message.from_user.id == TARGET_USER_ID:
        video_path = random.choice(VIDEO_FILES)
        if os.path.exists(video_path):
            with open(video_path, 'rb') as video:
                await message.reply_video(video, caption="Григорий написал — всем сюрприз!")
        else:
            await message.answer("Видео не найдено 😭")

async def main():
    print("Бот запущен и ждёт Григория...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
