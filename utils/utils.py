from datetime import date

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message

from keyboards import create_inline_kb
from lexicons import update_button, zodiac
from request import get_goroscope


def reverse_date(date: date) -> str:
    date_str = date.strftime('%Y-%m-%d')
    invert_date = date_str.split('-')[::-1]
    normal_date = f'{invert_date[0]}.{invert_date[1]}.{invert_date[2]}'
    return normal_date


async def get_last_message(bot: Bot, chat_id: int) -> Message:
    # Получаем последние 2 сообщения из истории чата
    messages = await bot.get_chat_history(chat_id, limit=1)

    if messages:
        last_message = messages[0]
        return last_message
    return None


async def send_goroscope_everyday(bot: Bot, state: FSMContext) -> None:

    data = await state.get_data()
    chat_id = data.get('chat_id')
    sign = data.get('sign')
    today = date.today()
    today_normal = reverse_date(today)
    goroscope = get_goroscope(zodiac[sign])
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=result,
            reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True)
