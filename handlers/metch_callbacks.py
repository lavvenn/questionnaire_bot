from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from data.db import get_user_data

from keyboards import inline

router = Router()

#функция которая возврощяет текст анекты пользователя по ID
def print_profile(user_data : dict) -> str:
    formated_text = []
    [formated_text.append(f"{key}: {value}") for key, value in user_data.items() if key != "photo"]
    return "\n".join(formated_text)


@router.callback_query(F.data.startswith("👍"))
async def metch(query: CallbackQuery, bot: Bot):
    from_user_data = get_user_data(query.from_user.id)
    liked_user_member_data = await bot.get_chat_member(chat_id=query.data[1:], user_id=query.data[1:])

    await bot.send_photo(chat_id= query.data[1:], photo= from_user_data["photo"], caption= f"{print_profile(from_user_data)} \n \n ник --> @{query.from_user.username}", reply_markup=inline.metch_kb)
    await query.message.edit_caption(caption=f"{print_profile(get_user_data(query.data[1:]))} \n \n ник --> @{liked_user_member_data.user.username}", reply_markup=inline.metch_kb)


@router.callback_query(F.data.startswith("👎"))
async def unmetch(query: CallbackQuery):

    await query.message.edit_caption(caption=f"{print_profile(get_user_data(query.data[1:]))}", reply_markup=inline.unmetch_kb)