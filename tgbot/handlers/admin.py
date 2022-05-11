from aiogram import Router
from aiogram.types import Message


admin_router = Router()

@admin_router.message(commands=["start"])
async def admin_start(message: Message):
    await message.reply("Привет, администратор!")