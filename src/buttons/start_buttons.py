from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


start_button_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊Подбор вакансий",callback_data="chats_list"),
            InlineKeyboardMarkup(text="📈Инструмент",url="https://t.me/Jobs_bridge"),
            InlineKeyboardMarkup(text="Разместить свою вакансию",callback_data="place_ad"),
        ]
    ]
)
