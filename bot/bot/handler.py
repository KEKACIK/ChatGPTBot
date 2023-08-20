from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from integrations.chatgpt import chat_gpt
from misc import bot

main_router = Router()


@main_router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    botname = (await bot.get_me()).full_name
    await message.answer(text="\n".join([
        f"Welcome to {botname}",
        f"Input your questions"
    ]))


@main_router.message()
async def all_message_handler(message: Message, state: FSMContext):
    answer = chat_gpt.get_answer(message.text)
    await message.answer(text=answer['choices'][0]['message']['content'])
