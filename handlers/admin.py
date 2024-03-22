from aiogram import Router, F 
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from utils.states import Admin

from keyboards import reply

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
    
@router.callback_query(F.data == 'print_photo')
async def print_photo(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text = "отправьте ссылку на изоброжение чтобы его распечатать", reply_markup= reply.admin_stop_state)
    await state.set_state(Admin.get_photo)

@router.message(Admin.get_photo)
async def print_photo(message: Message, state : FSMContext):
    if message.text == "⛔":
        await message.answer(text = "вы вышли из режима просмотра фото", reply_markup= reply.start_kb)
        await state.clear()

    else:
        try:
            await message.answer_photo(photo= message.text)
        except:
            await message.answer(text =  "отправленный вами текст не является ссылкой на фотографию")