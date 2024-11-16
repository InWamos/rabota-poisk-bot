import asyncio
import os
import logging
import sys

from handlers.start_handler import router
from handlers.callback_handlers import callback_router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router=router)
    dp.include_router(router=callback_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
