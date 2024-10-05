from aiogram.filters import Command, CommandStart
#from aiogram.fsm.context import FSMContext
from aiogram import Router, Dispatcher, F
from aiogram.types import Message, CallbackQuery, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
#from aiogram.enums import ParseMode

from constants import url


router = Router()
dp = Dispatcher()


def web_app_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="stocks",
        web_app=WebAppInfo(
            url=url
        )
    )
    return builder.as_markup()


@router.message(CommandStart())
async def start(msg: Message) -> None:
    await msg.reply(
        text="look!",
        reply_markup=web_app_builder()
    )
