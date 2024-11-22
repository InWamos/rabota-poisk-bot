import os
from aiogram import Router, F, types
from buttons.start_buttons import chats_button_markup, start_button_markup

MANAGER_NICKNAME = os.getenv("MANAGER_NICKNAME")

callback_router = Router()


@callback_router.callback_query(F.data == "chats_list")
async def return_chats_list(callback: types.CallbackQuery) -> None:
    message = callback.message
    if isinstance(message, types.Message):
        await message.edit_reply_markup(reply_markup=chats_button_markup)


@callback_router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery) -> None:
    message = callback.message
    if isinstance(message, types.Message):
        await message.edit_reply_markup(reply_markup=start_button_markup)


@callback_router.callback_query(F.data == "place_ad")
async def place_ad(callback: types.CallbackQuery) -> None:
    message = callback.message
    if isinstance(message, types.Message):
        await message.answer(
            text=f"Для размещения вакансии свяжитесь с менеджером {MANAGER_NICKNAME} с пометкой #РЕКЛАМА"
        )
