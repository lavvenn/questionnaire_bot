from aiogram import Router, F 
from aiogram.types import Message
from aiogram.filters import Command

from data.db import get_all_users

router = Router()

@router.message(Command('print_photo'))
async def print_photo_command(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIFw2X27YgwVUTnnE9YfrCpb7ZSY85CAAJ22DEbX2i5SyO9FZJFNkqxAQADAgADeAADNAQ")

@router.message(Command("db_0"))
async def db_get_users(message: Message):
    await message.answer(text = str(get_all_users()))
    print("значения получены")