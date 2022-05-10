import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, different_types

# ADMINS=563245011
# BOT_TOKEN=5217674922:AAGu5twmpt4NH3gCQ3ThWGEr_0tF-nonITU
# ip=localhost

# Run bot
async def main():
    bot = Bot(token="5217674922:AAGu5twmpt4NH3gCQ3ThWGEr_0tF-nonITU")
    dp = Dispatcher(bot)

    dp.include_router(questions.router)
    dp.include_router(different_types.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling


if __name__ == '__main__':
    asyncio.run(main())
    