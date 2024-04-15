import random

from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart

from keyboards import builder, inline, reply
from data.db import get_user_data, get_users_id_list

from utils.states import View_profiles

from config import EROR_TEXT, START_TEXT


router = Router()


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
    await message.answer(text= EROR_TEXT)


@router.message()
async def all_message(message: Message):
    await message.answer(text = EROR_TEXT) 

#<----callback handlers---->

@router.callback_query()
async def send_matched_profile(query: CallbackQuery,):
    await query.answer()
