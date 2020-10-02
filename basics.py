# # Python Tutorial for Beginners 2 Strings - Working with Textual Data

# # message = "Hello World"

# # print(message[6:])
# # print(message.upper())
# # print(message.lower())
# # print(message.count('l'))
# # print(message.find("orld"))
# # print(message.replace("World", "Universe"))

# # first_name = "Churays"
# # last_name = "Chicut"

# # greet = "{} {}, Welcome To Our Store!".format(first_name, last_name)
# # greet = f"{first_name.upper()} {last_name.upper()}, Welcome To Our Store!"
# # print(greet)

# # print(dir(first_name))
# # print(help(str.endswith)) -- most important python code

# ########################################################################################################

# #Slicing Lists and Strings

# #list[start:end:step]

# # list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #       0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# #     -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# # print(list[-9:])
# # print(list[-8:-2])
# # print(list[::-1])
# # print(list[2:-1:-1])
# # print(list[2:-1:2])
# # print(list[-2:1:-1])
# # print(list[-2:1:-2])

# # url = "http://google.com"

# # domain = url[-4:]
# # print(domain)

# # http = url[:7]
# # print(http)

# # google = url[7:-4]
# # print(google)

# ########################################################################################################

# #  String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates

# # format method with basic text
# # tag = "h1"
# # text = "This is a heading!"
# # element_node = '<{0}>{1}<{0}>'.format(tag, text)
# # print(element_node)

# # format method with a dictionary
# # person = {'name': "Marley", 'age': 21}
# # intro = 'My name is {0[name]} and l\'am {0[age]} years old!'.format(person)
# # print(intro)
# # print("{name} is the founder of Marlix and he is aged {age}".format(**person))

# # format method with a list
# # list = ["Marley", 21]
# # intro = 'Name: {0[0]}  ----  Age:{0[1]}'.format(list)
# # print(intro)

# # format method with a class
# # class Person():

# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p1 = Person("Churays", "29")
# # finality = '{0.name} is a founder of Finaliters and aged {0.age}'.format(p1)
# # print(finality)

# # format method with keyword arguments
# # print("{name} will be {age} this year!".format(name="Millz", age=30))

# # format to zero pad numbers

# # for num in range(1, 11):
# #   print("The value is: {:03}".format(num))

# # import datetime

# # my_date = datetime.datetime(2020,8,23,16,7,6)
# # date_format = "{:%B %d, %Y}".format(my_date)
# # print(date_format)

# #######################################################################################################

# # Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data

# # number = 3.75

# # print(round(number, 1)) # rounds to 1 decimal point
# # print(round(number))
# # print(abs(-19))

# ########################################################################################################

# # Python Tutorial for Beginners 4: Lists, Tuples, and Sets

# # courses = ["Math", "Physics", "CompSci", "Shona"]
# # courses_2 = ["Chem", "Biology"]
# # courses.extend(courses_2)
# # courses.sort(reverse=True)
# # print(courses)
# # print(courses.index("Biology"))
# # print('Art' in courses)

# # enumerate loops through a list and gives its element and index
# # for index, course in enumerate(courses, start=1):
# #     print(f"Index: {index}  Course: {course}")

# # list_str = ', '.join(courses)
# # courses_copy = list_str.split(", ")

# # print(list_str)
# # print(courses_copy)

# # print()
# # nums = [23, 1, 12, 0, 2, 3]
# # nums.sort(reverse=True)
# # print(nums)
# # print(min(nums))
# # print(max(nums))
# # print(sum(nums))

# #Empty list
# # empty_list = []
# # empty_list = list()

# #empty tuple
# # empty_tuple = ()
# # empty_tuple = tuple()

# #empty set
# # empty_set = {} # this isn't right. It is an empty dictionary
# # empty_set = set()

# #########################################################################################################

# # Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs

# # student = {'name': "Marley", 'age': 21, 'brothers': ['Millz', 'Fitz']}

# # student.update({'married': False, 'gpa': 4.8, 'hobby': "Coding"})
# # del student['name']

# # # print(student.pop('brothers'))
# # # print(student)

# # for key, value in student.items():
# #   print(f"Key: {key:20}  Value: {value}")

# # Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements

# # Object identity: keyword is  - used to check if two objects have the same id that is they occupy same memoory location

# # a = [1, 2, 3]
# # b = [1, 2, 3]

# # print(a == b) # true
# # print(a is b) # false
# # print(id(a)) # returns the memory location of a
# # print(id(b)) # returns the memory location of b

# # False Values:
# # False
# # None
# # Zero of any numeric type
# # Any empty sequence: for example, '', (), [].
# # Any empty mapping, for example, {}.

# # Python Tutorial for Beginners 8: Functions

# # def print_name(greeting, name="You"):
# #   return "{}, {}".format(greeting, name)

# # print(print_name("Hie",name="Marley"))

# # def(positional arguments, keyword arguments)

# # def student_info(*args, **kwargs):
# #   print(args)
# #   print(kwargs)

# # courses = list(('Math', 'Phys', 'Chem'))
# # info = {'name': 'Marley', 'age': 21, 'online': True}

# # student_info(courses, info)
# # student_info(*courses, **info)  # unpacking a list and a dictionary respectively

# # number_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# # def is_leap(year):
# #  """return True for leap years and False for non-leap years"""
# #  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# # def days_in_month(year, month):
# #   """Return number of days in that month in that year"""

# #   if not 1 <= month <= 12:
# #     return "invalid month!"

# #   if month == 2 and is_leap(year):
# #     return 29

# #   return number_days[month-1]

# # print(is_leap(2012))
# # print(days_in_month(2017, 2))
# # print(days_in_month(2020, 2))

# ######################################################################################################################

# # Python Tutorial: Variable Scope - Understanding the LEGB rule and global/nonlocal statements
# '''
# LEGB
# Local, Enclosing, Global, Built-in
# Local - are variables defined within a function
# Enclosing - are variables in the local scope of enclosing function
# Global - are variables defined at the top level of the module or explicitly declared global using the global keyword
# Built-in -- are just names that are pre-assigned in python. Note that functions in the built in can be overridden.
# '''

# #  import builtins

# # print(dir(builtins)) # important code to check functions in python builtin module
# # print(help(builtins.next)) # returns notes about how a specific function works

# # def set_global():
# #   global x  ###### access and modify global variable
# #   x = "local x"
# #   print(x)

# # print(pow(2,3))

# # def outer():
# #   x = "outer x"

# #   def inner():
# #     nonlocal x    #### accesses and modifies the enclosing variable
# #     x = "inner x"
# #     print(x)

# #   inner()
# #   print(x)

# # outer()

# # Programming Terms: First-Class Functions
# # First-Class Functions: "A programming language is said to have first-class functions if it treats functions as first-class citizens"
# # First-Class Citizen (Programming): " A first-class citizen (sometimes called first-class objects) in programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable."

# # if a function accepts other functions as arguments, return functions as a result are called higher order functions

# # def square(num):
# #   return num * num

# # def cubic(num):
# #   return num * num * num

# # def my_map(fun, arg_list):
# #   result = list()

# #   for num in arg_list:
# #     result.append(fun(num))

# #   return result

# # squared = my_map(square, [1, 2, 3, 4, 5])
# # print(squared)

# # cubiced = my_map(cubic, [1, 2, 3, 4, 5])
# # print(cubiced)

# # def html_wrap(tag):

# #   def wrap_text(text):
# #     print("<{0}>{1}<{0}>".format(tag, text))

# #   return wrap_text

# # h1_tag = html_wrap('h1')
# # h1_tag("This is a header tag!")

# # Closures
# # Wikipedia says, "A closure is a record storing a function together with an environment: a mapping associating each free variable of the function with the value or storage location to which the name was bound when the closure was created. A closure, unlike a plain function, allows the function to access those captured variables through the closure's reference to them, even when the function is invoked outside their scope."

# # A closure closes over the free variables from their environment

# # import logging

# # logging.basicConfig(filename="exam.log", level=logging.INFO)

# # def logger(func):

# #   def log_func(*args):
# #     logging.info("Reading \"{}\" with arguments({})".format(func.__name__, args))
# #     print(func(*args))

# #   return log_func

# # def add(x, y):
# #   return x + y

# # def subtract(x, y):
# #   return x - y

# # f_closure = logger(add)
# # s_closure = logger(subtract)

# # f_closure(2, 5)
# # f_closure(10, 2)

# # s_closure(10, 5)
# # s_closure(20, 10)

# # def outer(x, y):

# #   def inner():
# #     return x + y

# #   return inner

# # print(outer(2,16)())

# # Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions

# # Decorator is a function that takes another function as an argument adds some functionality and then returns another function without altering the source code of the function passed as an argument.

# # def decorator_func(func):
# #   def wrapper_func(*args, **kwargs):
# #     print("This will execute before ".format(func.__name__))
# #     return func(*args, **kwargs)

# #   return wrapper_func

# # @decorator_func
# # def greet():                    # greet =  decorator_func(greet)
# #   print("Hello World!")

# # @decorator_func
# # def sum(x, y):
# #   print(f"Sum of {x} and {y}: {x+y}")

# # greet()
# # sum(4, 5)

# # def my_logger(org_func):
# #   import logging
# #   logging.basicConfig(filename="{}.log".format(org_func.__name__),level=logging.INFO)

# #   def wrapper(*args, **kwargs):
# #     logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
# #     org_func(args, kwargs)

# #   return wrapper

# # @my_logger
# # def display_info(name, age):
# #   print("display_info ran with args: ({0}, {1})".format(name, age))

# # display_info("Marley", 21)

# # def my_timer(org_func):
# #   import time

# #   def wrapper(*args, **kwargs):
# #     t1 = time.time()
# #     result = org_func(*args, **kwargs)
# #     t2 = time.time() - t1
# #     print("{} ran : {} sec".format(org_func.__name__, t2))
# #     return result

# #   return wrapper

# # import time

# # @my_timer
# # def display_info(name, age):
# #   time.sleep(2)
# #   print("display info has args: ({}, {})".format(name, age))

# # display_info("Marley", 21)

# #####################################################################################################################

# #Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library

# # import my_module
# # index = my_module.find_value(courses, "Shona")

# # import my_module as mm_
# # index.mm_.find_value(courses, "Shona")

# # from my_module import *  //// This imports everything in the module but it's recommended as bad practise*/

# # import sys

# # from my_module import find_value, test

# # courses = ["History", "Math", "Shona", "Biology", "Chemistry"]

# # index = find_value(courses, "Shona")
# # print(index)
# # print(test)

# # print(sys.path)

# # useful standard library modules

# # import random
# # import math
# # import time
# # import logging
# # import datetime
# # import calendar

# # import os

# # print(os.getcwd())

# # Python Tutorial: Comprehensions - How they work and why you should be using them
# ######### List Comprehensions

# # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # l want "n*n" for each n in nums
# # my_list = []

# # for n in nums:
# #   my_list.append(n*n)

# # print(my_list)

# # list comprehension
# # list_comp = [n*n for n in nums]
# # print(list_comp)

# # using lambda and map
# # my_list = map(lambda n: n*n, nums)
# # print(list(my_list))

# # l want 'n' for each n in nums if 'n' is even

# # my_list = []

# # for n in nums:
# #   if n%2 == 0:
# #     my_list.append(n)

# # print(my_list)

# # list comprehension

# # print([n for n in nums if n%2 == 0])

# # using filter + lambda

# # my_list = filter(lambda n: n%2==0, nums)
# # print(list(my_list))

# # l want (letter, number) pair for each letter in 'abcd' and for each number in '0123'

# # my_list = []

# # for letter in 'abcd':
# #   for num in range(4):
# #     my_list.append((letter, num))

# # print(my_list)

# # list_comp = [(letter, num) for letter in 'abcd' for num in range(4)]
# # print(list_comp)

# ############## Dictionary Comprehensions

# # f_name = ["Lang", "Churays", "Stilles", "Terry", "Tawie"]
# # l_name = ["Marley", "Chicut", "Chaz", "Millz","Fitz"]

# # print(list(zip(f_name, l_name)))

# # my_dict = dict()

# # for name, surname in zip(f_name, l_name):
# #   my_dict[name] = surname

# # print(my_dict)
# # print()

# # dict_comp = {name: sur for name, sur in zip(f_name, l_name)}
# # print(dict_comp)

# ################### Set Comprehensions

# # nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
# # my_set = set()

# # for num in nums:
# #   my_set.add(num)

# # print(my_set)

# # Python Tutorial: Generators - How to use them and the benefits you receive
# # Generators don't hold the entire result in memory, it yields a result at a time by using next keyword

# # def square_numbers(nums):
# #   for num in nums:
# #     yield (num*num)

# # gen = square_numbers([1, 2, 3, 4, 5])

# # for num in gen:
# #   print(num)

# # Python Tutorial: OS Module - Use Underlying Operating System Functionality

# import os
# from datetime import datetime

# # print(dir(os))
# print(os.getcwd())

# # os.chdir('/home/runner/Corey-PythonTuts/package')
# # print(os.getcwd())

# # os.makedirs('OS-Demo/sub-demo')
# # os.removedirs('OS-Demo/sub-demo')
# # print(os.listdir())

# # os.rename("display_info.log", "print.log")
# # print(os.listdir())

# # mod_time = os.stat('print.log').st_mtime
# # print(datetime.fromtimestamp(mod_time))

# # for dirpath, dirnames, filenames in os.walk(os.getcwd()):
# #   print('''Dirpath: {0}
# # Dirnames: {1}
# # Filenames: {2}
# #   '''.format(dirpath, dirnames, filenames))

# # print(os.environ.get('HOME'))
# # file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# # print(file_path)

# # print(os.path.dirname('/marley/pygame.py'))
# # print(os.path.basename('/marley/pygame.py'))
# # print(os.path.exists('/marley/pygame.py'))
# # print(os.path.split('/marley/pygame.py'))
# # print(os.path.isfile('pygame.txt'))
# # print(os.path.isdir('/marley/pygame.txt'))
# # print(os.path.splitext('/marley/pygame.py'))

# # print()
# # print(dir(os.path))
# # print(help(os.path.isfile))

# #####################################################################################################################

# # Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones

# import datetime

# # d = datetime.date(2020, 6, 17)
# # print("Date: {}".format(d))
# # print(dir(datetime))
# # # print()
# # print(dir(datetime.date))
# # print()
# # print(dir(datetime))
# # print()
# # print(dir(datetime.timedelta))
# # print()
# # print(dir(datetime.time))
# # print()
# # print(dir(datetime.datetime)

# # tday = datetime.date.today()
# # print("Today: {}".format(tday))
# # print("Current Year: {}".format(datetime.date.today().year))
# '''
# date2 = date1 + timedelta
# timedelta = date1 + date2
# '''

# # tdelta = datetime.timedelta(days=7)
# # print(tdelta)

# # tday = datetime.date.today()
# # next_week = tday + tdelta
# # print("Next-week: {}".format(next_week))

# # bday  = datetime.date(2021, 6, 17)
# # till_bday = bday - tday
# # print('Days left: {}'.format(till_bday.days))
# # print("Seconds left: {}".format(till_bday.total_seconds()))

# # t = datetime.time(10, 20, 45, 300)
# # print("Time: {}".format(t.hour))

# # dt = datetime.datetime
# # print(help(dt.today))

# #####################################################################################################################

# # Python Tutorial: File Objects - Reading and Writing to Files

# # f = open('Customers.txt', 'r')

# # print(f.name)
# # print(f.mode)
# # print(dir(f))

# # f.close()

# with open('Customers.txt', 'r') as rf:
#     with open('Customers_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

#     # size_to_read = 10

#     # f_contents = f.read(size_to_read)

#     # while len(f_contents) > 0:
#     #   print(f_contents, end="*")
#     #   f_contents = f.read(size_to_read)

#     # for line in f:
#     #   print(line, end="")

#     # print(f.readline())
#     # print(f.readlines())
#     # file_contents = f.read()
#     # print(file_contents)

# ######################################################################################################

# # Python Tutorial: Generate Random Numbers and Data Using the random Module

# # import random

# # print(dir(random))
# # print('''

# # ''')

# # rand_num = random.random()
# # rand_num = random.uniform(1, 100) -- gives random float value between given range

# # rand_num = random.randint(1,6)
# # print(rand_num)

# # greetings = ['Hie', 'Hi', 'Hello', 'Holla', 'Nihao']
# # value = random.choice(greetings)
# # print("{}, Marley!".format(value))

# # colors = ["Red", "Green", "Blue"]
# # draw = random.choices(colors, weights=[18,18,2], k=10)
# # print("Draws: {}".format(draw))

# # deck_card = list(range(1,53))
# # random.shuffle(deck_card)
# # choosen = random.sample(deck_card, k=5)
# # print(choosen)

# ##############################################################################################################

# # Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files

# import csv

# # print(dir(csv))

# # with open('names.csv', 'r') as csv_file:
# #   csv_reader = csv.reader(csv_file)

# #   with open('new_names.csv', 'w') as new_file:
# #     csv_writer = csv.writer(new_file, delimiter="\t")

# #     for line in csv_reader:
# #       csv_writer.writerow(line)

# # with open('new_names.csv', 'r') as r_file:
# #   for line in  csv.reader(r_file, delimiter="\t"):
# #     print(line)

# # with open('names.csv', 'r') as r_file:

# #     with open('new_names.csv', 'w') as w_file:
# #       field_names = ["first_name", "last_name"]

# #       csv_dict_write = csv.DictWriter(w_file, fieldnames=field_names, delimiter='\t')

# #       csv_dict_write.writeheader()

# #       for line in csv.DictReader(r_file):
# #         del line['email']
# #         csv_dict_write.writerow(line)

# ###################################################################################################################

# # Python Tutorial: Real World Example - Parsing Names From a CSV to an HTML List

# # html_output = ''
# # names = []

# # with open('patreon.csv', 'r') as pat_file:
# #   csv_reader = csv.DictReader(pat_file)

# #   next(csv_reader)

# #   for line in csv_reader:
# #     if line["FirstName"] == "No Reward":
# #       break
# #     names.append(f"{line['FirstName']} {line['LastName']}")

# # html_output = f"<p>There are currently {len(names)} public contibutors.Thank you!<p>"

# # html_output += '\n<ul>'

# # for name in names:
# #   html_output += f"\n\t<li>{name}</li>"

# # html_output += '\n</ul>'

# # print(html_output)

# ###########################################################################################################################

# # Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)

# # .       - Any Character Except New Line
# # \d      - Digit (0-9)
# # \D      - Not a Digit (0-9)
# # \w      - Word Character (a-z, A-Z, 0-9, _)
# # \W      - Not a Word Character
# # \s      - Whitespace (space, tab, newline)
# # \S      - Not Whitespace (space, tab, newline)

# # \b      - Word Boundary
# # \B      - Not a Word Boundary
# # ^       - Beginning of a String
# # $       - End of a String

# # []      - Matches Characters in brackets
# # [^ ]    - Matches Characters NOT in brackets
# # |       - Either Or
# # ( )     - Group

# # Quantifiers:
# # *       - 0 or More
# # +       - 1 or More
# # ?       - 0 or One
# # {3}     - Exact Number
# # {3,4}   - Range of Numbers (Minimum, Maximum)

# #### Sample Regexs ####

# # [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

# import re

# # print(dir(re))
# print('''

# ''')

# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234

# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T

# cat
# pat
# mat
# bat
# '''

# sentence = 'Start a sentence and then bring it to an end'

# # pattern = re.compile(r'start', re.IGNORECASE)
# # matches = pattern.match(sentence)

# # pattern = re.compile(r'then')
# # matches = pattern.search(sentence)

# # print(matches)

# # pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# # pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# # matches = pattern.finditer(text_to_search)

# # for match in matches:
# #   print(match)

# # with open('data.txt', 'r') as r_file:
# #   contents = r_file.read()

# #   matches = pattern.finditer(contents)

# #   for match in matches:
# #     print(match)

# # emails = '''
# # CoreyMSchafer@gmail.com
# # corey.schafer@university.edu
# # corey-321-schafer@my-work.net
# # '''

# # pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# # matches = pattern.finditer(emails)

# # for match in matches:
# #   print(match)

# urls = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''

# # pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# # matches = pattern.finditer(urls)

# # subbed_urls = pattern.sub(r'\1\2\3', urls)
# # print(subbed_urls)

# #####################################################################################################################################################

# #Python Tutorial: Using Try/Except Blocks for Error Handling

# # try:
# #   f = open("Customers_copy.txt")

# #   if f.name == 'Customers_copy.txt':
# #     raise Exception

# # except FileNotFoundError as ex:
# #   print(ex)
# # except Exception as ex:
# #   print("This file is corrupted!")
# # else:
# #   print(f.read())
# #   f.close()
# # finally:
# #   print("Excuting finally...")

# ################################################################################################################################################

# # Python Quick Tip: F-Strings - How to Use Them and Advanced String Formatting

# # first_name = "Marley"
# # last_name = "Lang"

# # sentence = f"My name is {first_name.upper()} {last_name.upper()}"
# # print(sentence)

# person = {'name': "Jenn", 'age': 23}

# # sentence = "My name is {} and l am {} years old!".format(person["name"], person["age"])

# # sentence = f"My name is {person['name']} and l am {person['age']} years old!"

# # print(sentence)

# # for n in range(1,11):
# #   print(f"The value is now {n:02}")

# # print(f'The value of pi is {3.14159265:.3}')

# # import datetime
# # birthday = datetime.datetime(1999,6,17)
# # print(f'My birthday is on {birthday:%B %d, %Y}')

# ######################################################################################################################################

# # Python OOP Tutorial 1: Classes and Instances


# class Employee:

#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f'{self.first}.{self.last}@company.com'

#     def fullname(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         return f'{self.pay * Employee.raise_amount:.0f}'

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)

#     @staticmethod
#     def is_weekday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True


# emp1 = Employee("Marley", "lang", 50000)
# emp2 = Employee("Terry", "Millz", 60000)

# # print(emp1.pay)
# # print(emp1.apply_raise())

# # print(emp1.__dict__) # namespace of a class instance
# # print(Employee.__dict__) # namespace of a class
# # emp1.raise_amount = 1.08
# # print(emp1.__dict__)
# # print(emp2.__dict__)

# # Employee.set_raise_amt(1.10)
# # print(emp1.raise_amount)
# # print(emp2.raise_amount)
# # print(Employee.raise_amount)

# # emp_str_1 = "John-Doe-10000"
# # emp_str_2 = "Lucie-Star-20000"
# # emp_str_3 = "Bucky-Roberts-800000"

# # new_emp = Employee.from_string(emp_str_1)
# # print(new_emp.__dict__)

# # from datetime import datetime

# # today = datetime(2020, 9, 28)
# # print(emp1.is_weekday(today))


# ###########################################################################################################################################################################

# # Python OOP Tutorial 4: Inheritance - Creating Subclasses


# class Developer(Employee):
#   raise_amount = 1.10

#   def __init__(self, first, last, pay, prog_lang):
#     super().__init__(first, last, pay)
#     self.prog_lang = prog_lang


# class Manager(Employee):

#   def __init__(self, first, last, pay, employees=None):
#     super().__init__(first, last, pay)

#     if employees is None:
#       self.employees = []
#     else:
#       self.employees = employees

#   def add_emp(self, emp):
#     if emp not in self.employees:
#       self.employees.append(emp)

#   def remove_emp(self, emp):
#     if emp in self.employees:
#       self.employees.remove(emp)

#   def print_emps(self):
#     for emp in self.employees:
#       print(f'--> {emp.fullname()}')


# marley = Developer("Ronald","Marley",25000,"Python")
# # bill = Developer("Bill", "Gates", 1000000, "C++")

# # sue = Manager("Sue","Yang",900000000,[marley])
# # sue.add_emp(bill)
# # sue.remove_emp(marley)

# # print(sue.email)
# # sue.print_emps()


# # print(issubclass(Manager, Employee)) # checks if Manager subclass of Employee
# # print(isinstance(marley, Developer)) # checks if obj marley is an instance of Developer
# # print(isinstance(marley,Employee))
# ############################################################################################################################################################################################################################

# # Python OOP Tutorial 5: Special (Magic/Dunder) Methods

# # class Car:

# #   def __init__(self, b_name, mk_year, color):
# #     self.b_name = b_name
# #     self.mk_year = mk_year
# #     self.color = color

# #   def print_car(self):
# #     return f'{self.color} {self.b_name} made in {self.mk_year}'

# #   def __repr__(self):
# #     return f"Car({self.b_name}, {self.mk_year}, {self.color})"

# #   def __str__(self):
# #     return f"{self.print_car()}"


# # tesla = Car("Tesla", 2018, "red")
# # print(Car.__repr__(tesla))
# # print(tesla)


# # class Complex:

# #   def __init__(self, real, imag):
# #     self.real = real
# #     self.imag = imag

# #   def print_complex(self):
# #     if self.imag > 0 or self.imag == 0:
# #       return f"{self.real} + {self.imag}i"
# #     elif self.imag < 0:
# #       return  f"{self.real} - {self.imag}i"

# #   def __add__(self, other):
# #     return f"{self.real + other.real} + {self.imag +self.imag}i"


# # comp_1 = Complex(1, 2)
# # comp_2 = Complex(2, 2)
# # print(comp_1 + comp_2)

# ###############################################################################################################################################################################################################################

# # Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters

# # class Student:

# #   def __init__(self, name, id, major):
# #     self.name = name
# #     self.id = id
# #     self.major = major

# #   def stud_details(self):
# #     return f"Name: {self.name} \t Student id: {self.id} \t Major: {self.major}"

# #   @property                         --> Getter method
# #   def password(self):
# #     if self.name is not None or self.id is not None:
# #       return f"{self.name + str(self.id)}"

# #     return None


# #   @password.setter
# #   def password(self, pas):
# #     name, id = pas.split("_")
# #     self.name = name
# #     self.pas = pas

# #   @password.deleter
# #   def password(self):
# #     print("Reset password ... ")
# #     self.name = None
# #     self.id = None


# # marley = Student("Marley", 2019, "Software Engineering")

# # marley.password = "lang_4801"

# # print(marley.password)
# # del(marley.password)
# # print(marley.password)

# ################################################################################################################################################################################################################################

# # Python Tutorial: str() vs repr()

# # The goal of __repr__ is to be unambiguous
# # The goal of __str__ is to be readable


import math
import os
import sys

import pytz
import requests

print(sys.version)
print(sys.executable)

for tz in pytz.all_timezones:
    print(tz)