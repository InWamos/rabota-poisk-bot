import os

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from buttons.start_buttons import start_button_markup

START_PHOTO = os.getenv("START_PHOTO")

router = Router()


@router.message(CommandStart())
async def respond_to_start_commant(message: Message) -> None:
    await message.answer_photo(
        photo=START_PHOTO,
        caption="💼 Наш проект поможет найти вакансию по твоему запросу а также предоставит инструмент для карьерного роста и заработной платы📈",
        reply_markup=start_button_markup,
    )
