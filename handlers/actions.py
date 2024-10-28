from datetime import date

from aiogram import Bot, F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters import CheckCallbackIsUpdate
from keyboards import create_inline_kb
from lexicons import update_button, zodiac
from request import get_goroscope
from utils.utils import reverse_date

router = Router()


@router.callback_query(CheckCallbackIsUpdate())
async def update_callback(callback: types.CallbackQuery,
                          state: FSMContext, bot: Bot) -> None:
    """Хэндлер реагирует на колбэк 'update' и обвноляет горокоп в сообщении."""

    data = await state.get_data()
    sent_message_id = data.get('sent_message_id')
    sign = data.get('sign')

    today = date.today()
    today_normal = reverse_date(today)
    goroscope = get_goroscope(zodiac[sign])
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    await bot.edit_message_caption(callback.message.chat.id, sent_message_id,
                                   caption=result, reply_markup=inline_kb)


@router.message(F.content_type.in_({'voice', 'video', 'text'}))
async def reset(message: Message) -> None:
    """Хэндлер реагирует на неизвестные ему текст, видео, голос."""

    await message.answer('Извините, я не понял.')
