from aiogram import Bot
from aiogram.fsm.context import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.utils import send_goroscope_everyday


def create_jobs(scheduler: AsyncIOScheduler, bot: Bot,
                state: FSMContext) -> None:
    """Функция создает задачи, которые будут выполнены по запланированному
    времени."""

    scheduler.add_job(send_goroscope_everyday, 'cron',
                      hour=10, jobstore='default',
                      args=[bot, state])
