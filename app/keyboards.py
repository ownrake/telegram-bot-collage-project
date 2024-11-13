from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------------------------------------------------------------------------

helloKB = InlineKeyboardMarkup(inline_keyboard = [
[InlineKeyboardButton(text = "Продолжить", callback_data = "skipStartKB")]
])