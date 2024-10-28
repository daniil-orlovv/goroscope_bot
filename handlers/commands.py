from datetime import date

from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from keyboards import create_inline_kb, create_kb
from lexicons import start_buttons, update_button, zodiac
from request import get_goroscope
from utils.scheduler import create_jobs
from utils.utils import reverse_date

router = Router()


@router.message(CommandStart())
@router.message(Command('change_zodiac'))
async def start(message: Message, state: FSMContext,
                scheduler: AsyncIOScheduler, bot: Bot) -> None:
    """Хэндлер реагирует на команды /start, /change_zodiac и отправляет кнопки
    для выбора знака зодиака."""

    await state.clear()

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    await message.answer(text=('Приветствую! Выбери свой знак зодиака, чтобы я'
                               ' мог присылать тебе гороскоп на каждый день!'),
                         reply_markup=keyboard)
    await state.update_data(flag_msg=False)
    create_jobs(scheduler, bot, state)


@router.message(Command('reset'))
async def reset(message: Message, state: FSMContext) -> None:
    """Хэндлер реагирует на команду /reset и сбрасывает машину состояний."""

    await state.clear()
    await message.answer('Машина состояний сброшена! Можно начать сначала.')


@router.message(Command('update'))
async def update_command(message: Message,
                         state: FSMContext, bot: Bot) -> None:
    """Хэндлер реагирует на команду update и обновляет гороскоп в сообщении."""

    data = await state.get_data()
    sent_message_id = data.get('sent_message_id')
    sign = data.get('sign')
    flag = data.get('flag_msg')
    if not sign:
        await message.answer('Для получение или обновления гороскопа '
                             'сначала нужно выбрать свой знак зодиака!')
        return

    today = date.today()
    today_normal = reverse_date(today)
    goroscope = get_goroscope(zodiac[sign])
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    if flag is False:
        sent_message = await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=result,
            reply_markup=inline_kb)
        await state.update_data(sent_message_id=sent_message.message_id,
                                sign=sign, flag_msg=True)
    else:
        sent_message = await bot.edit_message_caption(
            message.chat.id, sent_message_id, caption=result,
            reply_markup=inline_kb)
        await state.update_data(sent_message_id=sent_message.message_id,
                                sign=sign)


@router.message(Command('clear_history'))
async def clear_history(message: Message, state: FSMContext, bot: Bot) -> None:
    """Хэндлер реагирует на команду /clear_history и удаляет все сообщения,
    кроме последнего."""

    data = await state.get_data()
    sent_message_id = data.get('sent_message_id')
    chat_id = message.chat.id

    deleted_count = 0
    for message_id in range(message.message_id, 0, -1):
        if message_id == sent_message_id:
            continue
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
            deleted_count += 1
        except Exception:
            pass
