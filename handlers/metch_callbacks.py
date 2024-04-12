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
    from_user = await get_user_data(query.from_user.id)
    to_user = await get_user_data(query.data[1:])

    await bot.send_photo(
        chat_id=query.data[1:],
        photo=from_user["photo"],
        caption=f"{format_user_data(from_user)} \n Username: @{query.from_user.username}",
        reply_markup=inline.metch_kb,
    )

    await query.message.edit_caption(
        caption=f"{format_user_data(to_user)} \n Username: @{to_user['telegram_name']}",
        reply_markup=inline.metch_kb,
    )


def format_user_data(user_data: dict) -> str:
    fields_to_exclude = ["photo", "telegram_name"]
    formatted_data = "\n".join(
        f"{key}: {value}" for key, value in user_data.items() if key not in fields_to_exclude
    )
    return formatted_data


@router.callback_query(F.data.startswith("👎"))
async def unmetch(query: CallbackQuery):

    await query.message.edit_caption(caption=f"{print_profile(get_user_data(query.data[1:]))}", reply_markup=inline.unmetch_kb)