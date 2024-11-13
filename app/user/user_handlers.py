from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.user.user_keyboards as userKB
import config as con

router = Router()

class InputString(StatesGroup):
    string = State()

# ------------------------------------------------------------------------------------------------------------------------------------------------

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(con.hello)

@router.message(Command("help"))
async def help(message: Message):
    await message.answer(con.help)

# ------------------------------------------------------------------------------------------------------------------------------------------------
