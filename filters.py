from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class CheckCallbackIsUpdate(BaseFilter):

    async def __call__(
            self,
            callback: CallbackQuery
    ) -> bool:
        """Метод проверяющий соответствие callback == "update"
        """

        return callback.data == 'update'
