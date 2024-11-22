import asyncio
import os
import logging
import sys

from handlers.start_handler import router
from handlers.callback_handlers import callback_router
from handlers.command_handlers import commands_router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


async def main() -> None:
    bot_token = os.getenv("BOT_TOKEN")
    if bot_token:
        bot = Bot(token=bot_token)
        dp = Dispatcher()
        dp.include_router(router=router)
        dp.include_router(router=callback_router)
        dp.include_router(router=commands_router)
        await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
