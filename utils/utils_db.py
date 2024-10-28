from sqlalchemy.orm import Session

from models.models import SignZodiac


def create_object_user(telegram_id: int, sign: str) -> SignZodiac:
    """Функция получает данные для создания объекта модели SignZodiac и
    возвращает его."""

    return SignZodiac(
        telegram_id=telegram_id,
        sign=sign
    )


def add_user_in_db(session: Session, telegram_id: int, sign: str) -> None:
    """Функция добавляет пользователя в БД, используя id и название знака."""

    object_for_db = create_object_user(telegram_id, sign)
    session.add(object_for_db)
    session.commit()


def check_exist_user_in_db(session: Session, telegram_id: int) -> bool:
    """Функция делает запрос в БД, проверяет наличие клиента в БД и отправляет
    True или False."""

    exist = session.query(SignZodiac.telegram_id).filter(
        SignZodiac.telegram_id == telegram_id).first()
    return True if exist else False
