from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

import text


class MainButtons:
    """
    The main buttons of the bot
    """
    @classmethod
    async def begin_buttons(cls, message: types.Message, builder: InlineKeyboardBuilder):
        builder.add(types.InlineKeyboardButton(
            text="Начнем",
            callback_data="exchanges_list")
        )

    @classmethod
    async def services_list_buttons(cls, message: types.Message, builder: InlineKeyboardBuilder):
        freelance_list = [
            {"resource_name": "Weblancer", "callback_data": "weblancer"},
            {"resource_name": "fl.ru", "callback_data": "fl"},
            {"resource_name": "Fiverr", "callback_data": "fiverr"},
        ]

        for item in freelance_list:
            builder.add(types.InlineKeyboardButton(
                text=item["resource_name"],
                callback_data=item["callback_data"])
            )
