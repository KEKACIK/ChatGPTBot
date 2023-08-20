from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from core.config import settings

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)
