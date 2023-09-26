from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

import keyboards
from parsers import weblancer_parser

router = Router()


@router.callback_query(F.data == "weblancer")
async def weblancer_settings_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    await keyboards.SettingButtons.main_settings_buttons(callback.message, builder)
    await callback.message.answer(
        "Хотите авторизоваться на Weblancer?",
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "skip")
async def get_weblancre_categories(callback: types.CallbackQuery):
    categories = await weblancer_parser.WeblancerScrapper.get_categories()
    builder = InlineKeyboardBuilder()
    # categories = ["1", "2", "3"]
    await keyboards.SettingButtons.categories_buttons(callback.message, builder, categories)

    await callback.message.answer(
        "Выберите категорию",
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
