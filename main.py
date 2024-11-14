import logging
import asyncio

from aiogram import Bot, Dispatcher

from config import api_token
from app.user.user_handlers import userRouter
from app.admin.admin_handlers import adminRouter
from app.database import database as db



logging.basicConfig(level = logging.INFO)
bot = Bot(token = api_token)
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    dp.include_router(userRouter)
    dp.include_router(adminRouter)
    await dp.start_polling(bot)

async def on_startup():
    await db.db_start()
    print("INFO.sqlite3.database:Database launched successfully")
    
if __name__ == "__main__":
    try:
        asyncio.run(on_startup())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nINFO.sqlite3.database:Database successfully disabled")
        print("INFO.aiogram.dispatcher:Stop polling - bot is offline")