import asyncio
import logging
import config




from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import Command
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode
from config import TOKEN




# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()




# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    
    kb = [
        [types.KeyboardButton(text="сказать Satoru")]

    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


#Функция старт которая дает приветствие и вызывает кнопку которая указаная выше
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>,",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )


@dp.message(F.text.lower() == "сказать satoru")
async def with_puree(message: types.Message):

    username = message.from_user.username


    await message.reply("Писюнькай", reply_markup=types.ReplyKeyboardRemove())
     # Send a message to yourself with the user's username
    await bot.send_message(chat_id=1079856563, text=f"Пользователь https://t.me/{username} хочет связаться с вами.")
    
    # Send a reply message to the user
    await message.answer("Спасибо за оставленную заявку, в скором времени мы с вами свяжемся.")



# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")

@dp.message(Command("help"))

async def cmd_help(message: types.Message):
     await message.answer("Привет! Я бот для обратной связи с Sosoiwb")
     await message.answer("Для того что бы написать ему следуйте инструкциям после нажатия /start ")

     await message.bot.send_dice(chat_id=message.chat.id , emoji='🎲')



@dp.message(Command("send"))
async def cmd_start(message: types.Message):


    # Obtain the user's username from the message
    username = message.from_user.username
    
    # Send a message to yourself with the user's username
    await bot.send_message(chat_id=1079856563, text=f"Пользователь https://t.me/ {username} хочет связаться с вами.")
    
    # Send a reply message to the user
    await message.answer("Спасибо за оставленную заявку, в скором времени мы с вами свяжемся.", reply_markup=kb)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())