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


def metch_unmetch_kd(user_id):
    builder = InlineKeyboardBuilder()

    buttons = ["👍","👎"]

    [builder.button(text=button, callback_data=f"{button}{user_id}") for button in buttons]

    return builder.as_markup()

