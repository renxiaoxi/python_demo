# name = input("What's your name? ")
# color = input("What color do you like? ")
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(name + ' likes ' + color)
# print(age)
# print(type(age))

# weight_pound = input('Your weight:(in pound) ')
# print('Your weight is ' + str(int(weight_pound)/2.205) + ' in kilograms')

#for triple quotes 
# contents = ''' 
# Hello Sherry

# this is Amy
# good

# '''

# print(contents)

# course = 'Hello, I am Sherry'
# print(course[0])
# print(course[-1])
# print(course[1:-2])
import string


# first_name = 'Sherry'
# last_name = 'Ge Shh'
# msg = f'{first_name}[{last_name}]is a good girl.'
# print(msg)

# print(msg.find('e'))
# print(msg.replace('S','C'))
# print('S' in msg)
# print('C' in msg)

# print(string.ascii_lowercase)

# print(1 + 12)
# print(9 / 3) #get the float
# print(10 / 3) #get the float
# print(22 // 3)   #get the integer
# print(199 % 33) # get the mod
# print(10 ** 2) # get the power

# print(10 * 3 % 2)

# print(round(2.453434))

# import math
# print(math.ceil(2.9))
# print(math.isclose(12.106,12.001,abs_tol=0.5))

# has_good_credit = True
# house_price = 1
# down_payment = ''
# if has_good_credit:
#     down_payment = house_price * .1
# else:
#     down_payment = house_price * .2
# print(f'down_payment is ${down_payment} in m')


# print(str.capitalize('sherry'))

# data = 'sherry'
# print(f'my name is {data}')
# name = input('Create your nick name: ')
# if len(name) < 3 :
#     # if len(name) < 3 :
#     print('The name is quite short, please check it and enter it again!')
#     # else:
# elif len(name) > 15 : 
#     print('The name is quite long, please check it and enter it again! ')
# else:
#     print(f'{str.capitalize(name)}, It looks good!')

# try:
#     weight = float(input('weight: '))
#     unit = input('(L)bs or (K)g:' )
#     if (unit.upper() == 'L'):
#         weight *= .45
#         print(f'{weight} in (K)g')
#     elif unit.upper() == 'K':
#         weight /= .45
#         print(f'{weight} in (L)bs')
# except:
#     print('Weight only includes numbers. Please check it and enter again!')

# my_number = 8
# total_time = 3
# curr_time = 0
# while curr_time < total_time:
#     your_number = int(input('Guess: (please enter in numbers)'))
#     curr_time += 1
#     if(your_number == my_number):
#         # curr_time = total_time
#         print('You are right!')
#         break
# else:
#     print('You are wrong!')

# order = input('> ')
# if order == 'help':
#     print('''
#     start - to start the car
#     stop - to stop the car
#     quit - to exit
#     ''')
#     second_order = input ('> ')
#     while second_order != 'quit':
#         if second_order == 'start':
#             print('to start the car')
#             second_order = input ('> ')
#         elif second_order == 'stop':
#             print('to stop the car')
#             second_order = input ('> ')
#         else:
#             print('I don\'t understand that')
#             second_order = input ('> ')
#     else:
#         print('to exit')
        
# order = ''
# is_started = False
# is_stopped = False
# while True:
#     order = input('> ').lower()
#     if order == 'start':
#         if is_started:
#             print('You\'v already started the car!')
#         else:
#             print('Car started!')
#             is_started = True
#             is_stopped = False
#     elif order == 'stop':
#         if is_stopped:
#             print('You\'v already stopped the car!')
#         else:
#             print('Car stopped')
#             is_stopped = True
#             is_started = False
#     elif order == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif order == 'quit':
#         break
#     else:
#         print('I don\'t understand')
        

# for item in range(2,50,3):
#     print(item)

# prices = [10,20,30]
# total = 0
# for price in prices:
#     total += price
# print(f'total is {total}')

# pattern = [5,2,5,2,2]
# for x in pattern:
#     print('*'*x)

# _list = [2,454,23,212,666,35,234]
# max = _list[0]
# for num in _list[1:]:
#     if num > max:
#         max = num

# print(f'max is {max}')

# remove duplicate item in a list

# _list = ['sherry','eric','class','helen','english','sherry','eric']

# for item in _list:
#     while _list.count(item) > 1:
#         _list.remove(item)


# print(f'_list: {_list}')

# matrix = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
#     ]
# for row in matrix:
#     for item in row:
#         print(item)
# import pymysql.cursors

# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()


# array = [1,3, 2,23,5,44, 5,2,4,44,1, 5]
# #print(set(array))

# for item in array:
#     if array.count(item) > 1:
#         array.remove(item)
# array.sort()
# print(f'array is {array}')
    

# number = input('phone: ')
# # 1 2 3 4 one two three four
# number_dict = {
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four',
#     '5':'five',
#     '6':'six',
#     '7':'seven',
#     '8':'eight',
#     '9':'nine'
# }
# numberlist = ['zero','one','two','three','four','five','six','seven','eight','nine']
# list = []
# str = ''

# for num in number:
#     str += number_dict.get(num,'!') + ' '
#     # list.append(number_dict[num])

# print(str)

# words = input('> ')

# emoji = {
#     ":)":"😁"
# }
# str = ''
# words = words.split(' ')
# for item in words:
#     str += emoji.get(item, item) + ' '
# # print(str)

# try:
#     num = input('> ')
#     print(5/int(num))
# except ZeroDivisionError:
#     print(f'number cannot be {num}')

# class people:
#     def __init__(self,name):
#         self.name = name
#     def talk(self, words):
#         print(f'{words},I\'m {self.name}')

# sherry = people('Sherry')
# sherry.talk('hello')

# class Book:
#     def __init__(self,title):
#         self.title = title
#     def functions(self):
#         print('\nBook Is For Education\n'+'*'*30)

# class Novel(Book):
#     def __init__(self,title,hero, heroine,):
#         self.hero = hero
#         self.heroine = heroine
#         self.title = title
#         Book.__init__(self,title)
    

#     def descripation(self):
#         Book.functions(self)
#         print(f'Title: {self.title}\nHero: {self.hero}\nHeroine: {self.heroine}\n'+'*'*30)
    
# my_world = Novel('My World','Eric','Sherry')
# my_world.descripation()


#Basic Function is: {Book.functions()}\n

#module

# from utils import find_max

# list = [23,34,12,124,56,332,23,123,4556,343]

# print(f'The max number is {find_max(list)}')

import random

todo_list = ['literature','python','javascript','webassembly','css','vue','ocarina']

print(random.choice(todo_list))