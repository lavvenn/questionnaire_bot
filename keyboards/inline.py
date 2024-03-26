from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

metch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ взаимный лайк", callback_data="metch_kb")]
])

unmetch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❌ отклонено", callback_data="metch_kb")]
])


