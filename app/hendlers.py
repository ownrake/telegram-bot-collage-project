from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# import app.keyboards as kb
from app.keyboards import userKeyboards
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

@router.message(Command("panel"))
async def panel(message: Message):
    await message.answer(con.panel)

# ------------------------------------------------------------------------------------------------------------------------------------------------
