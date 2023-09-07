from loguru import logger

import misc
from bot.handler import main_router
from db.init_db import init_db


def setup():
    misc.dp.include_router(main_router)


async def on_startup():
    setup()

    try:
        await init_db()
    except ConnectionRefusedError:
        logger.error("Failed to connect to db")
        exit(0)

    logger.info("Bot started")


async def on_shutdown():
    logger.info("Bot stopped")


if __name__ == '__main__':
    misc.dp.startup.register(on_startup)
    misc.dp.shutdown.register(on_shutdown)
    misc.dp.run_polling(misc.bot)
