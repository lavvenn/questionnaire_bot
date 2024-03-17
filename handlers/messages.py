from aiogram import Router, F 
from aiogram.types import Message

router = Router()

@router.message(F.text == 'gg')
async def gg(message: Message):
    await message.answer(text = 'ggggggggg')