from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from buttons.start_buttons import start_button_markup

router = Router()


@router.message(CommandStart())
async def respond_to_start_commant(message: Message) -> None:
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMpZzfojI-6s3bMcB5w016YB3yJMQ0AAqHvMRuw5LlJdYueJXgY_jMBAAMCAANzAAM2BA",
        caption="💼 Наш проект поможет найти вакансию по твоему запросу а также предоставит инструмент для карьерного роста и заработной платы📈",
        reply_markup=start_button_markup,
    )
