from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def respond_to_start_commant(message: Message) -> None:
    await message.reply_dice()