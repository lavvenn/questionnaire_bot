from aiogram import Router, F 
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from data.db import get_all_users


router = Router()

#<----message handlers---->
@router.message(Command('print_photo'))
async def print_photo_command(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIFw2X27YgwVUTnnE9YfrCpb7ZSY85CAAJ22DEbX2i5SyO9FZJFNkqxAQADAgADeAADNAQ")



#<----callback handlers---->
@router.callback_query(F.data == 'all_users')
async def print_all_users(query: CallbackQuery):
    await query.message.answer(str(get_all_users()))
    await query.answer(text='all users printed👍🏿')
    await query.message.delete()
    