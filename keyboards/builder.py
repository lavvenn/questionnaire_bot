from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton


#<----reply keyboars---->
def profile(text: str | list): 
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text = txt) for txt in text]

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True)



#<----inline keyboars---->
def admin_panel():
    builder = InlineKeyboardBuilder()
    
    admin_comand_list = ['all_users', 'print_photo']

    [builder.button(text=command, callback_data=command) for command in admin_comand_list]

    return builder.as_markup()

def next_profile():
    builder = InlineKeyboardBuilder()

    builder.button(text = "⏭next", callback_data= 'view_next_profile')
    builder.button(text = "🛑stop", callback_data= 'stop_view_profile')

    return builder.as_markup()

