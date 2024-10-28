from datetime import date

from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import FSInputFile, Message
from sqlalchemy.orm import Session

from keyboards import create_inline_kb, create_kb
from lexicons import signs_descriptions, start_buttons, update_button, zodiac
from request import get_goroscope
from states import SignZodiac
from utils.utils import reverse_date
from utils.utils_db import add_user_in_db, check_exist_user_in_db

router = Router()


@router.message(F.text == '♈️')
async def oven_desc(message: Message, state: FSMContext, session: Session,
                    bot: Bot) -> None:
    """Хэндлер реагирует на текст ♈️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'oven'
    await state.set_state(SignZodiac.oven)
    await state.update_data(sign='oven')
    await message.answer(text=signs_descriptions['oven'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♉️', StateFilter(default_state))
async def telec_desc(message: Message, state: FSMContext, session: Session,
                     bot: Bot) -> None:
    """Хэндлер реагирует на текст ♉️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'telec'
    await state.set_state(SignZodiac.telec)
    await message.answer(text=signs_descriptions['telec'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♊️', StateFilter(default_state))
async def gemini_desc(message: Message, state: FSMContext, session: Session,
                      bot: Bot) -> None:
    """Хэндлер реагирует на текст ♊️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'bliznecy'
    await state.set_state(SignZodiac.bliznecy)
    await message.answer(text=signs_descriptions['bliznecy'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♋️', StateFilter(default_state))
async def cancer_desc(message: Message, state: FSMContext, session: Session,
                      bot: Bot) -> None:
    """Хэндлер реагирует на текст ♋️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'rac'
    await state.set_state(SignZodiac.rac)
    await message.answer(text=signs_descriptions['rac'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♌️', StateFilter(default_state))
async def leo_desc(message: Message, state: FSMContext, session: Session,
                   bot: Bot) -> None:
    """Хэндлер реагирует на текст ♌️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'lev'
    await state.set_state(SignZodiac.lev)
    await message.answer(text=signs_descriptions['lev'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♍️', StateFilter(default_state))
async def virgo_desc(message: Message, state: FSMContext, session: Session,
                     bot: Bot) -> None:
    """Хэндлер реагирует на текст ♍️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'deva'
    await state.set_state(SignZodiac.deva)
    await message.answer(text=signs_descriptions['deva'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♎️', StateFilter(default_state))
async def libra_desc(message: Message, state: FSMContext, session: Session,
                     bot: Bot) -> None:
    """Хэндлер реагирует на текст ♎️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'vesy'
    await state.set_state(SignZodiac.vesy)
    await message.answer(text=signs_descriptions['vesy'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♏️', StateFilter(default_state))
async def scorpio_desc(message: Message, state: FSMContext, session: Session,
                       bot: Bot) -> None:
    """Хэндлер реагирует на текст ♏️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'scorpion'
    await state.set_state(SignZodiac.scorpion)
    await message.answer(text=signs_descriptions['scorpion'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♐️', StateFilter(default_state))
async def sagittarius_desc(message: Message, state: FSMContext,
                           session: Session, bot: Bot) -> None:
    """Хэндлер реагирует на текст ♐️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'strelec'
    await state.set_state(SignZodiac.strelec)
    await message.answer(text=signs_descriptions['strelec'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♑️', StateFilter(default_state))
async def capricorn_desc(message: Message, state: FSMContext,
                         session: Session, bot: Bot) -> None:
    """Хэндлер реагирует на текст ♑️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'kozerog'
    await state.set_state(SignZodiac.kozerog)
    await message.answer(text=signs_descriptions['kozerog'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♒️', StateFilter(default_state))
async def aquarius_desc(message: Message, state: FSMContext, session: Session,
                        bot: Bot) -> None:
    """Хэндлер реагирует на текст ♒️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'vodoley'
    await state.set_state(SignZodiac.vodoley)
    await message.answer(text=signs_descriptions['vodoley'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)


@router.message(F.text == '♓️', StateFilter(default_state))
async def pisces_desc(message: Message, state: FSMContext, session: Session,
                      bot: Bot) -> None:
    """Хэндлер реагирует на текст ♓️ и отправляет описание
    знака зодиака."""

    keyboard = create_kb(start_buttons['adjust'], *start_buttons['buttons'])
    telegram_id = message.from_user.id
    sign = 'ryby'
    await state.set_state(SignZodiac.ryby)
    await message.answer(text=signs_descriptions['ryby'],
                         reply_markup=keyboard)
    user_exist = check_exist_user_in_db(session, telegram_id)
    if not user_exist:
        add_user_in_db(session, telegram_id, sign)
    goroscope = get_goroscope(zodiac[sign])
    today = date.today()
    today_normal = reverse_date(today)
    photo = FSInputFile(f"images/{sign}.jpg")
    result = f'<b>{today_normal}</b>\n\n{goroscope}'
    inline_kb = create_inline_kb((1, 1), **update_button)
    sent_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=result,
        reply_markup=inline_kb)
    await state.update_data(sent_message_id=sent_message.message_id,
                            sign=sign, flag_msg=True, chat_id=message.chat.id)
