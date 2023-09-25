from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

import text

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Начнем",
        callback_data="exchanges_list")
    )

    await message.answer(
        text.WELCOME_TEXT,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "exchanges_list")
async def exchanges_list_handler(callback: types.CallbackQuery):
    freelance_list = [
        {"resource_name": "Weblancer", "callback_data": "weblancer"},
        {"resource_name": "fl.ru", "callback_data": "fl"},
        {"resource_name": "Fiverr", "callback_data": "fiverr"},
    ]
    builder = InlineKeyboardBuilder()

    for item in freelance_list:
        builder.add(types.InlineKeyboardButton(
            text=item["resource_name"],
            callback_data=item["callback_data"])
        )
    await callback.message.answer(
        text.EXCHANGES_LIST,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "weblancer")
async def weblancer_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
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

    await callback.message.answer(
        "Хотите авторизоваться на Weblancer?",
        reply_markup=builder.as_markup(),
    )




#         await message.answer("Some text here", reply_markup=builder.as_markup())

#         weblancer_profile = await auth_weblancer.get_profile()
#         if weblancer_profile == "Р СџР С•Р В»РЎРЉР В·Р С•Р Р†Р В°РЎвЂљР ВµР В»РЎРЉ Р Р…Р Вµ Р В°Р Р†РЎвЂљР С•РЎР‚Р С‘Р В·Р С•Р Р†Р В°Р Р…":
#             await message.answer("Р СџР С•Р В»РЎРЉР В·Р С•Р Р†Р В°РЎвЂљР ВµР В»РЎРЉ Р Р…Р Вµ Р В°Р Р†РЎвЂљР С•РЎР‚Р С‘Р В·Р С•Р Р†Р В°Р Р…")
#             await auth_weblancer.make_auth()
#         else:
#             await message.answer(f"Р вЂ™РЎвЂ№ Р В°Р Р†РЎвЂљР С•РЎР‚Р С‘Р В·Р С•Р Р†Р В°Р В»Р С‘РЎРѓРЎРЉ Р Р…Р В° Weblancer Р С”Р В°Р С” - {weblancer_profile.pageProps.user.first_name}")
#         await message.send_copy(chat_id=message.chat.id)
