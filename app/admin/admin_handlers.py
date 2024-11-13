from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.admin.admin_keyboards as adminKB
import config as con

adminRouter = Router()

class InputString(StatesGroup):
    string = State()

# ------------------------------------------------------------------------------------------------------------------------------------------------

@adminRouter.message(Command("panel"))
async def panel(message: Message):
    await message.answer(con.panel)

# ------------------------------------------------------------------------------------------------------------------------------------------------
