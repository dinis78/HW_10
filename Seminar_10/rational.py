# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# logging.basicConfig(level=logging.INFO)
import telebot
from telebot import types
from fractions import Fraction
import telebot
from telebot import types
from fractions import Fraction

# async def first_namber (message: types.Message):
#     await message.answer('Введите первое число через /')
    
#def get_text_messages(message):

# a= int(input('ведите числитель перврго числа '))
# b= int(input('введите занаменатель первого числа '))
# c= int(input('ведите числитель второго числа '))
# d= int(input('введите занаменатель второго числа '))

# # global x 
# # global y 
x=Fraction(a, b)
y=Fraction(c, d)


operation = input('введите символ операции, + - *  / ')
if operation  != '+' or operation!= '-' or operation != '*' or operation != '/':
    print('неизвесная операция')
    operation = input('введите символ операции, + - * /  ')

def sum_fraction(x, y):
    result=x+y
    return result

def subtract_fraction(x, y):
    result=x-y
    return result

def multiply_fraction(x, y):
    result=x*y
    return result

def divide_fraction(x, y):
    result=x/y
    return result       

if operation == '+':
    result=sum_fraction(x, y)  


elif operation == '-':
    result=subtract_fraction(x, y)  


elif operation == '*':
    result=multiply_fraction(x, y)  


elif operation == '/':
    result=divide_fraction(x, y)   


print (x, operation, y, '=', result)   
