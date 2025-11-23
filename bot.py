from aiogram import Bot, Dispatcher, types
import asyncio
import random
import os

API_TOKEN = '7636498052:AAH9M_7P8cW9eK8z9YcX7vB6nL5mK4jH3gF'
TARGET_USER_ID = 5620273741

VIDEO_FILES = ['pisy.mp4']  # ← потом зальёшь своё видео с таким же именем

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def trigger(message: types.Message):
    if message.from_user and message.from_user.id == TARGET_USER_ID:
        video = random.choice(VIDEO_FILES)
        if os.path.exists(video):
            with open(video, 'rb') as v:
                await message.reply_video(v, caption="Гриша написал — всем привет от него!")
        else:
            await message.answer("Видео пока нет, но я уже готовлю сюрприз…")

async def main():
    print("Бот запущен и ждёт Гришу…")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
