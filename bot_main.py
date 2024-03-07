import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from My_token import TOKEN
from dialog import start_handler
from dialog.windows import dialog

logging.basicConfig(level=logging.INFO)


async def main():
    storage = MemoryStorage()
    bot = Bot(TOKEN)
    dp = Dispatcher(storage=storage)
    dp.include_router(start_handler.router)
    dp.include_router(dialog)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def bot_run():
    asyncio.run(main())


if __name__ == '__main__':
    bot_run()
