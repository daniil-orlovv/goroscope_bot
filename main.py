import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

from config import Config, load_config
from handlers import actions, commands, descriptions
from middleware import DBMiddleware

jobstores = {
    'default': MemoryJobStore()
}


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler = AsyncIOScheduler(jobstores=jobstores)
    engine = create_engine(
            'sqlite:///sqlite3.db',
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10
        )
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(descriptions.router)
    dp.include_router(actions.router)
    dp.update.outer_middleware(DBMiddleware())
    dp.workflow_data.update({'engine': engine, 'bot': bot, 'config': config,
                             'scheduler': scheduler})

    await bot.delete_webhook(drop_pending_updates=True)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
