from aiogram.types import (KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def create_kb(adjust: list, *args, **kwargs) -> InlineKeyboardMarkup:
    """Функция получает аргументы для создания клавиатуры и возвращает ее."""
    kb_builder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = []

    if kwargs:
        for key, value in kwargs.items():
            buttons.append(KeyboardButton(
                    text=key,
                    callback_data=value
                ))
    if args:
        for item in args:
            buttons.append(KeyboardButton(
                text=item
            ))
    kb_builder.add(*buttons)
    kb_builder.adjust(*adjust)
    return kb_builder.as_markup(resize_keyboard=True)


def create_inline_kb(method_kb, *args, **kwargs) -> InlineKeyboardMarkup:
    """Функция получает аргументы для создания инлайн-клавиатуры и возвращает
    ее."""
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if kwargs:

        for key, value in kwargs.items():
            if value.startswith('https'):
                buttons.append(InlineKeyboardButton(
                    text=key,
                    url=value
                ))
            else:
                buttons.append(InlineKeyboardButton(
                        text=key,
                        callback_data=str(value)
                    ))

    if args:
        for value in args:
            buttons.append(InlineKeyboardButton(
                        text=f'{value}',
                        callback_data=f'{value}'
            ))

    kb_builder.add(*buttons)
    kb_builder.adjust(*method_kb)
    return kb_builder.as_markup(resize_keyboard=True)
