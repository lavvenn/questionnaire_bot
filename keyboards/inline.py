from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

prikol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="да", callback_data='rofl'), InlineKeyboardButton(text='ну... а вдруг', callback_data='rofl')]
])

