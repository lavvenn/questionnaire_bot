from aiogram import Router, F 
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.states import Form

from keyboards.builder import profile

from keyboards import reply

from data.db import add_user_questionaire

router = Router()

@router.message(F.text == '📝создать/редактировать анкету')
async def fill_profile(message : Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(text = 'введи имя', reply_markup= profile(message.from_user.first_name))


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Form.age)
    await message.answer(text = 'введите свой возраст')


@router.message(Form.age)
async def from_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age = message.text)
        await state.set_state(Form.gender)
        await message.answer(text = 'выберите ваш пол', reply_markup= profile(["M", 'F']))
    else:
        await message.answer(text='ЦИФРАМИ ПИШИ')


# TODO: доделать проверку пола 



@router.message(Form.gender)
async def incorrect_form_gender(message: Message, state: FSMContext):
    await state.update_data(gender = message.text)
    await state.set_state(Form.about)
    await message.answer(text = 'о себе')


@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    await state.update_data(about = message.text)
    await state.set_state(Form.photo)
    await message.answer(text = 'отправьте фото ')


@router.message(Form.photo, F.photo)
async def from_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id

    await state.update_data(photo = photo_file_id)

    data = await state.get_data()   

    formated_text = []
    [
        formated_text.append(f"{key}: {value}")
        for key, value in data.items() if key != "photo"
    ]
    await message.answer_photo(photo_file_id, "\n".join(formated_text), reply_markup=reply.start_kb)
   

    print(data)

    add_user_questionaire(message.from_user.id, data)

    await state.clear()


@router.message(Form.photo, ~F.photo)
async def incorrect_from_photo(message: Message, state: FSMContext):
    await message.answer(text = 'ФОТКУ СКИНЬ')
