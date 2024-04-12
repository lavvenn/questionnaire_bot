import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN

from handlers import admin, commands, messages, questionaire, view_profilles, metch_callbacks

bot = Bot(TOKEN)
dp = Dispatcher()



async def main():
    """
    Main function that includes all routers and starts polling.
    """

    # Include all routers into dispatcher
    dp.include_routers(
        messages.router,
        metch_callbacks.router,
        questionaire.router,
        admin.router,
        view_profilles.router,
        commands.router,
    )

    # Start polling with bot to handle updates
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())