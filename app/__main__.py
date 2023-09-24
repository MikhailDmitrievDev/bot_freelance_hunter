from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, config
from app.loader import dp

from app import middlewares, filters, handlers


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(config.SUPERUSER_IDS)


if __name__ == '__main__':
    utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    executor.start_polling(
        dp, on_startup=on_startup, skip_updates=config.SKIP_UPDATES
    )




#         await message.answer("Some text here", reply_markup=builder.as_markup())

#         weblancer_profile = await auth_weblancer.get_profile()
#         if weblancer_profile == "РџРѕР»СЊР·РѕРІР°С‚РµР»СЊ РЅРµ Р°РІС‚РѕСЂРёР·РѕРІР°РЅ":
#             await message.answer("РџРѕР»СЊР·РѕРІР°С‚РµР»СЊ РЅРµ Р°РІС‚РѕСЂРёР·РѕРІР°РЅ")
#             await auth_weblancer.make_auth()
#         else:
#             await message.answer(f"Р’С‹ Р°РІС‚РѕСЂРёР·РѕРІР°Р»РёСЃСЊ РЅР° Weblancer РєР°Рє - {weblancer_profile.pageProps.user.first_name}")
#         await message.send_copy(chat_id=message.chat.id)
