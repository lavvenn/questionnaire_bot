from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="📝создать/редактировать анкету"), KeyboardButton(text="👤 моя анкета")],
    [KeyboardButton(text="🔍смотреть анкеты")],
    [KeyboardButton(text="❓ помощь")],
], resize_keyboard=True)

view_profiles_kb = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="👍"), KeyboardButton(text="👎"), KeyboardButton(text = "❌")],
], resize_keyboard=True)

admin_stop_state = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text = "⛔")],
])