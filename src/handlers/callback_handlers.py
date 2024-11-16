from aiogram import Router, F, types
from buttons.start_buttons import chats_button_markup, start_button_markup

callback_router = Router()


@callback_router.callback_query(F.data == "chats_list")
async def return_chats_list(callback: types.CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=chats_button_markup)


@callback_router.callback_query(F.data == "back_to_main")
async def return_chats_list(callback: types.CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=start_button_markup)


@callback_router.callback_query(F.data == "place_ad")
async def return_chats_list(callback: types.CallbackQuery) -> None:
    await callback.message.reply(
        text="Для размещения вакансии свяжитесь с менеджером @BEATNGO с пометкой #РЕКЛАМА"
    )
