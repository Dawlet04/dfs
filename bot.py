


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from my_btns import registration,main_menu,admin_menu   
from datas import save_users,show_users
from aiogram.client.session.aiohttp import AiohttpSession

api = '8250792358:AAHO5YvumhY2lL3fu4rM5hgqW25bnnOb6Yc'
bot = Bot(api)
dp = Dispatcher()
admins= 7976107229

class AutoMobile(StatesGroup):
    name = State()
    phone_number = State()
    address = State()

class Advertisement(StatesGroup):
    text = State()
    photo = State()
@dp.message(Command('start'))
async def send_hi(sms: types.Message):
    users = await show_users()
    for i in users:
        if sms.from_user.id in i:
            await sms.answer(text='c вовращением',reply_markup=main_menu),
            break

    if sms.from_user.id == admins:
        await sms.answer("  администратор!", 
                         reply_markup=admin_menu)
    else:
        await sms.answer("Добро пожаловать ", 
                         reply_markup=main_menu)
    



@dp.message(F.text == 'Registration')
async def start_adding(sms: types.Message, state: FSMContext):
    await sms.answer("напишите ваше имя.")
    await state.set_state(AutoMobile.name)


@dp.message(AutoMobile.name)
async def save_name(sms: types.Message, state: FSMContext):
    await state.update_data(name=sms.text)
    await sms.answer("  Теперь укажите ваш номер телефона")
    await state.set_state(AutoMobile.phone_number)


@dp.message(AutoMobile.phone_number)
async def save_phone(sms: types.Message, state: FSMContext):
    if not sms.text.isdigit() or len(sms.text)<9:
        await sms.answer(text='Вы не ввели свой номер телефона')
    else:
        await state.update_data(phone_number=sms.text)
        await sms.answer(" Теперь напишите ваш адрес ")
        await state.set_state(AutoMobile.address)


@dp.message(AutoMobile.address)
async def save_address(sms: types.Message, state: FSMContext):
    await state.update_data(address=sms.text)
    datas = await state.get_data()
    print(datas)
    await save_users(
        id=sms.from_user.id,
        name=datas['name'],
        phone_numbeer=datas['phone_number'],
        adddres=datas['address'],
    )

    await state.clear()


@dp.message(F.text=='Реклама') 
async def start_adding(sms: types.Message, state: FSMContext):
    await sms.answer("напишите текст.")
    await state.set_state(Advertisement.photo) 
@dp.message(Advertisement.photo)
async def save_photo(sms:types.Message,state:FSMContext):
    await state.update_data(photo=sms.photo[0].file_id)
    magliwmatlar = await state.get_data()

    print(magliwmatlar)
    await bot.send_photo(
        chat_id=admins,
        photo=magliwmatlar['photo'],
        caption=f'''{magliwmatlar['text']}
'''
    )

    await state.clear()
  




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())