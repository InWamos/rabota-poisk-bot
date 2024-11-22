import os
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database_methods.json_database_methods_impl import JsonDatabaseMethodsImpl

ADMINS = os.getenv("ADMINS")
ADMINS_PARSED = ADMINS.split(",") if ADMINS else []

commands_router = Router()

@commands_router.message(Command("size"))
async def get_db_size(message: Message) -> None:
    
    user_id = str(message.from_user.id) if message.from_user else None

    if user_id in ADMINS_PARSED:
        db_engine = JsonDatabaseMethodsImpl()
        await message.answer(text=f"Users in the db: {db_engine.get_users_amount()}")