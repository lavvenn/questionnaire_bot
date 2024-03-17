import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN

from handlers import commands, messages, questionaire, debug

bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    dp.include_routers(
        messages.router,
        commands.router,
        questionaire.router,
        debug.router,
    )
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())