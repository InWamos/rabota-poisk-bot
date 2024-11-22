import os

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from buttons.start_buttons import start_button_markup

from database_methods.json_database_methods_impl import JsonDatabaseMethodsImpl

START_PHOTO = os.getenv("START_PHOTO")

router = Router()


@router.message(CommandStart())
async def respond_to_start_commant(message: Message) -> None:
    if START_PHOTO and message.from_user:
        await message.answer_photo(
            photo=START_PHOTO,
            caption="💼 Наш проект поможет найти вакансию по твоему запросу а также предоставит инструмент для карьерного роста и заработной платы📈",
            reply_markup=start_button_markup,
        )
        json_db = JsonDatabaseMethodsImpl()
        json_db.add_user(str(message.from_user.id))
