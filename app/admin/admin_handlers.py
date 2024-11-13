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
    if message.from_user.id in con.adminID:
        await message.answer(con.panel, reply_markup = adminKB.startPanel)
    else:
        await message.answer("Не хватает прав доступа для использования данной команды")

# ------------------------------------------------------------------------------------------------------------------------------------------------

@adminRouter.callback_query(F.data == "updSchlude")
async def updSchlude(callback: CallbackQuery):
    await callback.message.answer("Выберите неделю для изменения", reply_markup = adminKB.inputWeek)

    if F.data == "evenWeek":
        await callback.message.answer("Func is work!")
    elif F.data == "oddWeek":
        pass
    else:
        await callback.message.answer("Ошибка выбора недели. Попробуйте заново")