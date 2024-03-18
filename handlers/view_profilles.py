import random

from aiogram import Router, F 
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.states import View_profiles

from keyboards.builder import next_profile

from data.db import get_user_data, get_users_id_list

router = Router()

@router.message(F.text == "🔍смотреть анкеты(норм)")
async def view_profiles(message : Message, state: FSMContext):
    await state.set_state(View_profiles.view)
    await state.update_data(unviewed = get_users_id_list())
    await message.answer(text = "чтобы начать смотреть анкеты нажмите next", reply_markup=next_profile())
    
    
@router.message(View_profiles.view)
async def view_profiles_text(message: Message, state: FSMContext):
    await message.answer(text = "тут на кнопки нажимать надо")

@router.callback_query(View_profiles.view)
async def view_profiles_callback(query: CallbackQuery, state: FSMContext):
    if query.data == "view_next_profile":
        try:
            state_data = await state.get_data()

            unviewed_list = state_data['unviewed']
            
            user_id = random.choice(unviewed_list)

            unviewed_list.remove(user_id)

            user_data = get_user_data(user_id)

            formated_text = []
            [formated_text.append(f"{key}: {value}") for key, value in user_data.items() if key != "photo"]


            await query.message.answer_photo(photo= user_data.pop("photo"), caption= "\n".join(formated_text), reply_markup=next_profile())
            await query.answer(text='следующая анкета',)
        except IndexError:
            await query.message.answer('это были все анкеты')
            await query.answer(text = 'конец')
    elif query.data == "stop_view_profile":
        await state.clear()
        await query.message.answer(text = "вы вышли из просмотра анкет")
        await query.answer()
