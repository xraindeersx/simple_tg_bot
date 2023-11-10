import asyncio

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import Command

bot1 = Bot(token="")
bot2 = Bot(token="")

dp = Dispatcher(bot=bot1)
dp2 = Dispatcher(bot=bot2)


@dp.message(Command("start"))
@dp2.message(Command("start"))
async def cmd_start(message: types.Message):
    bot_name = await message.bot.get_me()
    await message.answer(f"Это бот {bot_name.first_name}, вы написали {message.text}")


async def main():
    await asyncio.gather(dp.start_polling(bot1), dp2.start_polling(bot2))


if __name__ == "__main__":
    asyncio.run(main())
