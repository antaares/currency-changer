from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS

class IsAdmin(BoundFilter):
    async def check(self, message):
        return message.from_user.id in ADMINS