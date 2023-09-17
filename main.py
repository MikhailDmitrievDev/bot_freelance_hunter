
import asyncio

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from weblancer_parse.wl_scrapper import AuthWeblance as auth_weblancer
from config import TOKEN_BOT

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, dsa!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # await auth_weblancer.make_auth()
        weblancer_profile = await auth_weblancer.get_profile()
        await message.answer(f"Вы авторизовались на Weblancer как - {weblancer_profile.pageProps.user.first_name}")
        await message.send_copy(chat_id=message.chat.id)
    except TypeError as e:
        print(e)
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN_BOT, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Start bot")
    asyncio.run(main())
