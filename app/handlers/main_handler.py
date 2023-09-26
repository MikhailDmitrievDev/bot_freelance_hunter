from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

import text
import keyboards

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """
    Method for start
    """
    builder = InlineKeyboardBuilder()
    await keyboards.MainButtons.begin_buttons(message, builder)
    await message.answer(
        text.WELCOME_TEXT,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "exchanges_list")
async def exchanges_list_handler(callback: types.CallbackQuery):
    """
    Method get exchanges list
    """
    builder = InlineKeyboardBuilder()
    await keyboards.MainButtons.services_list_buttons(callback.message, builder)
    await callback.message.answer(
        text.EXCHANGES_LIST,
        reply_markup=builder.as_markup(),
    )
