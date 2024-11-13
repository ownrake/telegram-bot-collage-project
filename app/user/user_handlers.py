from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.user.user_keyboards as userKB
import config as con

userRouter = Router()

class InputString(StatesGroup):
    string = State()

# ------------------------------------------------------------------------------------------------------------------------------------------------

@userRouter.message(CommandStart())
async def start(message: Message):
    await message.answer(con.hello)

@userRouter.message(Command("help"))
async def help(message: Message):
    await message.answer(con.help)

@userRouter.message(Command("mass"))
async def mass(message: Message):
    await message.answer(con.mass)

# ------------------------------------------------------------------------------------------------------------------------------------------------
