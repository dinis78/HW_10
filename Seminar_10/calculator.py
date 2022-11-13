import asyncio
import logging
from aiogram import Bot, Dispatcher, types
logging.basicConfig(level=logging.INFO)
import rational
from fractions import Fraction
import re
# bot = Bot(token='5749336976:AAEf9JstvgZNf2QHI26UdI-rklxzY0VNcJY')
dp = Dispatcher()

@dp.message(commands=['start'])
async def cmd_start (message: types.Message):
    await message.answer(F'Привет {message.from_user.first_name}!\nКаким калькулятором хочешь возпользоваться?\n/rational\n/comprehensive')

@dp.message(commands=['rational'])
async def cmd_rational (message: types.Message):
    await message.answer('Введите первое число через /, через запятую введите второе число /')
     
@dp.message_handler()
async def first_namber(msg: types.Message):
        mes = msg.text
        items= re.split('/|,', mes)
        a=int(items[0])
        b=int(items[1])
        c=int(items[2])
        d=int(items[3])
        x=Fraction(a, b)
        y=Fraction(c, d)
        await bot.send_message(msg.from_user.id, f'{x}+{y}={x+y}')
        await bot.send_message(msg.from_user.id, text='Введите первое число через /')
@dp.message_handler()
async def second_namber(msg: types.Message):
        mes = msg.text
        items= mes.split('/')
        c=int(items[0])
        d=int(items[1])
        await bot.send_message(msg.from_user.id, f'{first_namber}+{c}+{d}={first_namber+c+d}')


    

    
#@bot.message_handler(content_types=['text'])



@dp.message(commands=['comprehensive'])
    

    # msg = dp.message(message.text)
    # await message.answer(f'{msg}')




    # await message.answer('Введите второе число через /')
    


@dp.message(commands=['comprehensive'])
  



# Розыгрыш №201


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  

# app = ApplicationBuilder().token("5749336976:AAEf9JstvgZNf2QHI26UdI-rklxzY0VNcJY").build()
# print('server start')

# app.add_handler(CommandHandler("start", culc_comand))
# app.add_handler(CommandHandler("rational", one_first_number))
# app.add_handler(CommandHandler())



# app.run_polling()