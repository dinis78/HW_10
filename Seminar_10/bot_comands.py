import telebot
from telebot import types
from fractions import Fraction
import rational
bot = telebot.TeleBot('5749336976:AAEf9JstvgZNf2QHI26UdI-rklxzY0VNcJY')
storage = {}

def init_storage(user_id):
  storage[user_id] = dict(first_number=None, second_number=None)

# def store_number(user_id, key, value):
#   storage[user_id][key] = dict(value=value)

# def get_number(user_id, key):
#   return storage[user_id][key].get('value')

@bot.message_handler(func=lambda m: True)
def start(message):
  init_storage(message.from_user.id)
  bot.reply_to(message, 'Введите первое число через / ')
  bot.register_next_step_handler(message, namber_one)

# def plus(message):
#       if message.text == '+':
#          bot.reply_to(message,'Введите первое число через / ')
#          bot.register_next_step_handler(message, namber_one)
      

def namber_one(message):
        
        mes = message.text
        items= mes.split('/')
        a=int(items[0])
        b=int(items[1])
        x=Fraction(a, b)
        # first_number=x
        #store_number(message.from_user.id, 'first_number', first_number)
        bot.reply_to(message, 'Введите второе число через /')
        bot.register_next_step_handler(message, namber_two)

def namber_two(message):
       
        mes = message.text
        items= mes.split('/')
        c=int(items[0])
        d=int(items[1])
        y=Fraction(c, d)
        # second_number=y
        #store_number(message.from_user.id, 'second_number', second_number)
        bot.reply_to(message, '')
        bot.register_next_step_handler(message, namber_two)



        # namber_1 = get_number(message.from_user.id, 'first_number')
        # namber_2 = get_number(message.from_user.id, 'second_number')
#         result_plus = namber_1 + namber_2
# bot.reply_to(message, f'{namber_1}+{namber_2}= {result_plus}')


# def plus(message):
#       if message.text == '+':
#          bot.reply_to(message,'Введите первое число через / ')
#          bot.register_next_step_handler(message, namber_one)       

      




if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
    #bot.infinity_polling()