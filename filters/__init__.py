from aiogram import Dispatcher
from filters.is_admin import IsAdmin

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    #dp.filters_factory.bind(is_admin)
    pass
