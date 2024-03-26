import random

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.states import View_profiles

from keyboards.reply import view_profiles_kb, start_kb
from keyboards.builder import metch_unmetch_kd

from data.db import get_user_data, get_users_id_list

next_profile_query_list = ["view_next_profile", "profile_like", "profile_dislike"]

router = Router()

#функция которая возврощяет текст анекты пользователя по ID
def print_profile(user_data : dict) -> str:
    formated_text = []
    [formated_text.append(f"{key}: {value}") for key, value in user_data.items() if key != "photo"]
    return "\n".join(formated_text)



@router.message(F.text == "🔍смотреть анкеты")
async def view_profiles(message : Message, state: FSMContext):
    await state.set_state(View_profiles.view)
    #создаём список непросмотренных анкет
    unviewed_list = get_users_id_list(without = message.from_user.id)

    #выбираем из этого списка рандомный ID для отрисовки анкеты 
    selected_user_id = random.choice(unviewed_list)
    #удоляем этот ID из списка потому что он уже просмотрен
    unviewed_list.remove(selected_user_id)
    #записываем список без этого ID в state.data["unviewed_list"]
    await state.update_data(unviewed = unviewed_list)

    #получаем данные выбраного пользователя по ID 
    selected_user_data = get_user_data(selected_user_id)

    #отрисовываем анкеты выбранного пользователя
    await message.answer_photo(photo= selected_user_data.pop("photo"), caption= print_profile(selected_user_data), reply_markup=view_profiles_kb)  
    #записываем выбраный ID в state.data["state.data["selectad_user"]"]
    await state.update_data(selected_user_id = selected_user_id)
    
    
    
@router.message(View_profiles.view)
async def view_profiles_text(message: Message, state: FSMContext, bot: Bot):
    if message.text == "👍":

        state_data = await state.get_data()

        from_user_data = get_user_data(message.from_user.id)

        await bot.send_photo(chat_id = state_data["selected_user_id"], photo=from_user_data["photo"], caption= print_profile(from_user_data), reply_markup=metch_unmetch_kd(message.from_user.id))
        await bot.send_message(chat_id = state_data["selected_user_id"], text= "⬆кому то понравилась ваша анкета⬆")

        try:
            unviewed_list = state_data['unviewed']

            selected_user_id = random.choice(unviewed_list)

            unviewed_list.remove(selected_user_id)

            user_data = get_user_data(selected_user_id)

            await message.answer_photo(photo= user_data.pop("photo"), caption= print_profile(user_data))
            await state.update_data(selected_user_id = selected_user_id)

        except IndexError:
            await message.answer('это были все анкеты', reply_markup= start_kb)
            await state.clear()


    elif message.text == "👎":
        try:
            state_data = await state.get_data()
            
            unviewed_list = state_data['unviewed']

            selected_user_id = random.choice(unviewed_list)

            unviewed_list.remove(selected_user_id)

            user_data = get_user_data(selected_user_id)

            await message.answer_photo(photo= user_data.pop("photo"), caption= print_profile(user_data))
            await state.update_data(selected_user_id = selected_user_id)
        except IndexError:
            await message.answer('это были все анкеты', reply_markup= start_kb)
            await state.clear()     


    elif message.text == "❌":
        await state.clear()
        await message.answer(text = "вы вышли из просмотра анкет", reply_markup= start_kb)

    else:
        await message.answer(text = "вы сейчас находитесь в режиме просмотра анкет. Если хотите выйти нажмите на '❌' на клавиатуре бота")
    


@router.callback_query(View_profiles.view)
async def view_profiles_callback(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text = "вы сейчас находитесь в режиме просмотра анкет. Если хотите выйти нажмите на '❌' на клавиатуре бота")
    await query.answer(text="ничё тут не нажимай"),

