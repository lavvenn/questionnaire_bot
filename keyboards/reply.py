from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="📝создать/редактировать анкету"), KeyboardButton(text="👤 моя анкета")],
    [KeyboardButton(text="🔍смотреть анкет")],
    [KeyboardButton(text="❓ помощь")],
], resize_keyboard=True)

rofl_kb = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="📝создать/редактировать анкету"), KeyboardButton(text="👤 моя анкета")],
    [KeyboardButton(text="🔍смотреть анкеты(норм)")],
    [KeyboardButton(text="❓ помощь")],
], resize_keyboard=True)