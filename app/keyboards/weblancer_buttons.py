from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

class SettingButtons:
    """
    Weblancer settings
    """
    @classmethod
    async def main_settings_buttons(cls, message: types.Message, builder: InlineKeyboardBuilder):
        """
        Main settings buttons
        """
        builder.add(types.InlineKeyboardButton(
            text="Авторизоваться",
            callback_data="auth")
        )
        builder.add(types.InlineKeyboardButton(
            text="Пропустить",
            callback_data="skip")
        )
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="exchanges_list")
        )

    @classmethod
    async def auth_buttons(cls, message: types.Message, builder: InlineKeyboardBuilder):
        ...

    @classmethod
    async def categories_buttons(cls, message: types.Message, builder: InlineKeyboardBuilder, categories: list):
        """
        Categories buttons
        """
        for item in categories:
            builder.add(types.InlineKeyboardButton(
                text=item.get("name"),
                callback_data="1")
            )
