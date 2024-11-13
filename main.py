import logging
import asyncio

from aiogram import Bot, Dispatcher

from config import api_token
from app.user.user_handlers import userRouter
from app.admin.admin_handlers import adminRouter

# ------------------------------------------------------------------------------------------------------------------------------------------------

logging.basicConfig(level = logging.INFO)
bot = Bot(token = api_token)
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    dp.include_router(userRouter)
    dp.include_router(adminRouter)
    await dp.start_polling(bot)

# ------------------------------------------------------------------------------------------------------------------------------------------------
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nINFO.aiogram.dispatcher:Stop polling - bot is offline")