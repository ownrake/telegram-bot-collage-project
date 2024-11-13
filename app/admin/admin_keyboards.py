from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------------------------------------------------------------------------

startPanel = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Изменить расписание", callback_data = "updSchlude")]
])

inputWeek = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Чётная неделя", callback_data = "evenWeek")],
    [InlineKeyboardButton(text = "Нечтная неделя", callback_data = "oddWeek")]
])

evenWeekDays = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Понедельник", callback_data = "evenMonday")],
    [InlineKeyboardButton(text = "Вторник", callback_data = "evenTuesday")],
    [InlineKeyboardButton(text = "Среда", callback_data = "evenWednesday")],
    [InlineKeyboardButton(text = "Четверг", callback_data = "evenThursday")],
    [InlineKeyboardButton(text = "Пятница", callback_data = "evenFriday")],
    [InlineKeyboardButton(text = "Суббота", callback_data = "evenSaturday")]
])