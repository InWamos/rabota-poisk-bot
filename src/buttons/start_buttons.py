import os
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

INSTRUMENT_LINK = os.getenv("INSTRUMENT_LINK")

start_button_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📊Подбор вакансий", callback_data="chats_list")],
        [InlineKeyboardButton(text="📈Инструмент", url=INSTRUMENT_LINK)],
        [
            InlineKeyboardButton(
                text="Разместить свою вакансию", callback_data="place_ad"
            )
        ],
    ]
)

chats_button_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Работа Киев", url="https://t.me/rabota_kyiv_desk")],
        [
            InlineKeyboardButton(
                text="Работа Днепр", url="https://t.me/rabota_dnepr_desk"
            ),
            InlineKeyboardButton(
                text="Работа Харьков", url="https://t.me/rabota_harkov_desk"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Работа Украина", url="https://t.me/rabota_ukraine_desk"
            ),
            InlineKeyboardButton(
                text="Работа Онлайн", url="https://t.me/rabota_online_desk"
            ),
        ],
        [InlineKeyboardButton(text="<-- Назад", callback_data="back_to_main")],
    ]
)
