from loguru import logger

import misc
from bot.handler import main_router


def setup():
    misc.dp.include_router(main_router)


async def on_startup():
    setup()

    logger.info("Bot started")


async def on_shutdown():
    logger.info("Bot stopped")


if __name__ == '__main__':
    misc.dp.startup.register(on_startup)
    misc.dp.shutdown.register(on_shutdown)
    misc.dp.run_polling(misc.bot)
