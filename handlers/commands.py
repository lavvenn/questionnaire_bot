import random

from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart

from keyboards import builder, inline, reply
from data.db import get_user_data, get_users_id_list

from utils.states import View_profiles

from config import EROR_TEXT, ADMIN_ID_LIST


router = Router()

START_TEXT = """
**Привет!** 😊
Я твой *личный помощник* в создании и просмотре анкет. Моя функция - облегчить тебе процесс поиска и создания анкет, делая его **быстрым и удобным**. Для начала работы можешь воспользоваться следующими командами:
- *Создать анкету*: Создай свою анкету, указав основные данные о себе.
- *Просмотреть анкеты*: Посмотри анкеты других пользователей, чтобы найти интересующие тебя варианты.
- *Поиск анкет*: Найди анкету, соответствующую твоим критериям.
Если у тебя возникнут вопросы или понадобится помощь, не стесняйся спрашивать! Я здесь, чтобы помочь тебе. Удачи! 🤖✨
"""

#<----message handlers---->
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=START_TEXT, parse_mode='Markdown', reply_markup= reply.start_kb)


@router.message(F.text == "👤 моя анкета")
async def my_profile_command(message: Message):
    user_data = get_user_data(message.from_user.id)
    formated_text = []
    [formated_text.append(f"{key}: {value}") for key, value in user_data.items() if key != "photo"]
    await message.answer_photo(photo= user_data.pop("photo"), caption= "\n".join(formated_text))


@router.message(F.text == "❓ помощь")
async def norm_kb(message: Message):
    await message.answer(text= "чел, ну тут же всё очевидно. если тебе с ЭТИМ нужно помощь то советую тебе просто больше не заходить в интернет")


@router.message(Command("admin"))
async def debug_command(message: Message):
    if message.from_user.id in ADMIN_ID_LIST:
        await message.answer(text="выберите нужную функцию", reply_markup=builder.admin_panel())
        await message.delete()
    else:
        await message.answer(text = EROR_TEXT)


@router.message()
async def all_message(message: Message):
    await message.answer(text = EROR_TEXT) 

#<----callback handlers---->

# TODO доделать штуки

# @router.callback_query(F.data == "👍")
# async def send_matched_profile(query: CallbackQuery, bot: Bot):
#     await bot.get_chat_member()
