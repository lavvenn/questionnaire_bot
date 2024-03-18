from aiogram.fsm.state import StatesGroup, State



# class Main(StatesGroup):
#     start = State()
class View_profiles(StatesGroup):
    view = State()


class Form(StatesGroup):
    name = State()
    age = State()
    gender  =State()
    about = State()
    photo = State()