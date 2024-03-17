from aiogram import Router, F 
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart

from data.db import get_user_data


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="""
hello bro
""", parse_mode='MarkdownV2')
    
@router.message(Command("my_profile"))
async def my_profile_command(message: Message):
    user_data = get_user_data(message.from_user.id)
    
    await message.answer_photo(photo= user_data.pop("photo"), caption=str(user_data))