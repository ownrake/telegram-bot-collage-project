from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------------------------------------------------------------------------

startPanel = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Изменить расписание", callback_data = "updSchlude")]
])

inputWeek = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Чётная неделя", callback_data = "evenWeek")],
    [InlineKeyboardButton(text = "Нечтная неделя", callback_data = "oddWeek")]
])