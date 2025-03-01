import asyncio
from aiogram import Bot, Dispatcher
import config
import handlers

bot = Bot(token=config.TOKEN)
dp = Dispatcher()  # Aiogram 3.x da botni dispatcher ichiga kiritmaymiz

# Handlerlarni ro‘yxatdan o‘tkazish
dp.include_router(handlers.router)

async def main():
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
