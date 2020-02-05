# Day Notes

# Print "Hello, world!" to your terminal

print("Hello World")

''' Intro to Python I - Guided Project
    This document contains examples for CS Intro to Python, module 1. Examples
    focus on Python syntax & semantics plus the usage of lists, dicts, sets,
    and tuples.
'''
# How do we print something to the console?
print("Hello, world!")
print('"hello, world!", said Austen')
print("Aren't you excited about Python")
# With f-strings?
# TODO

name = "Austen"
#avoid -p-> print ("hello" + name)
print(f'hello {name}')
# Given an "out" string length 4, such as "<<>>", and a word, return a new 
# string where the word is in the middle of the out string, e.g. "<<word>>".
# (from CodingBat)
def make_out_word(out, word):
    # TODO
    return out[:2] + word + out[2:]


# print(make_out_word('<<>>', 'Yay')) # → '<<Yay>>'
# print(make_out_word('<<>>', 'WooHoo') # → '<<WooHoo>>'
# print(make_out_word('[[]]', 'word')) # → '[[word]]'
# Given an array of ints length 3, return the sum of all the elements.
# (from CodingBat)
def sum3(nums):
    # TODO
    pass
# print(sum3([1, 2, 3])) # → 6
# print(sum3([5, 11, 2]) # → 18
# print(sum3([7, 0, 0])) # → 7
# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at 
# least one 7). Return 0 for no numbers.
# (from CodingBat)
def sum67(nums):
    sum = 0
    for n in nums:
        if n == 6:
            #ignore until we find a 7, remove?
        elif n == 7:
            #start adding ints to sum again, remove?
        else:
            if not skip:
                sum += n
                if skip: #if skipp == True

        return sum

   
# print(sum67([1, 2, 2])) # → 5
# print(sum67([1, 2, 2, 6, 99, 99, 7])) # → 5
# print(sum67([1, 1, 6, 7, 2])) # → 4
# Create a new list containing the squares of all values in `numbers`with a 
# list comprehension
numbers = [1, 2, 3, 4, 5]
print(numbers)

squares = [num*num for num in numbers]
print(squares)

# the equivalent of...
squares_two= []
for num in numbers:
    squares_two.append(num*num)

print(squares_two)

# We can also use list comprehensions to filter!
# Create a new list containing only the even values of `numbers`

evens = [num for num in numbers if num % 2 == 0]
print(evens)



# the equivalent of...
evens_two = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens_two)
# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they 
# are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(names)
                #new value             for loop         filter
names_with_s = [name.capitalize() for name in names if name[0].lower() == 's']
print[names_with_s]

#grab all names that start with S
#fix capitalization

names_w = []
for n in numbers:
    if name[0].lower() == 's':
        names.append(n)
print(names_w/s)

#list

#dictionary

person = { "name": "Joe", "age": 35, "city": "Chicage"}

#Set
# no duplicates, unordered
users = {3343, 34343, 2332}

#Tuple



# Day 2

# Dictionaries

students = {}

# adding to the dictionary
students[342]= 'Sam'
students[344]= 'Jordan'
print(students)
# updateing the dictinoary
students[342]= 'Mike'
print(students)


# pass by value or reference

n = 5
nums = [1,2,3]


def mult2(x): # x is a single integer value to be doubled
    return x * 2

def mult2_list(x): # x is a list of interger values to be doubled
    for i in range(len(x)):
        x[i ]*= 2
    return x
    

print(mult2(n))
print(n)

print(mult2_list(nums))
print(nums) 



# Tackling larger problems ie algorithms

#have steps to break down larger problems
# 1. understand- ask questions
# 2. plan things out
# 3. execute
# 4. reflect 
# /is this implementation as good as I make it
# 
# 

# Uper- given a number of people, number of pizza, and number of slices per pizza, write a function to evenly divide the slices between each person


#1. understand 
#- How do we know #s? (pass as args in the functions)
#- Is everyone eating? (yes)
#- Min/Maxes? (positint int values)
#- Half/slices? (no)
#- cost per slice? (n/a)
#-return # slicesper person? (yes + # of leftovers that no one gest :())
#


#2. Plan
def divide_pizza(people, pizza, slices):
    total_slices = pizza * slices
    # Find total number of slice (pizza slices)
    # do division
        # Find "floor" (slices per person)
    slices_per_person = total_slices //poeple
    # Find remainder (leftovers)
    leftover = total_slices % people
    # Return info as a string
    return f'Each person get {slices_per_person} slices and there are {leftovers}'

print(divide_pizza(4, 2, 8)) # 4 slices, 0 leftovers
print(divide_pizz(5, 3, 8)) # 4 slices, 4 lefovers

 # UPER - Prompt a user to enter three, uique numbers as input, print out 
# which number is the largest of the three. 
# 1. Understand
#what type of input
#return format string or a list
# user_data = input("prompt")

# 2. Plan
# a way to prompt the user()
# where the numbers come from()
# need to know a user()
# need an input()
# a way to store each number()
# how to compare numbers ()
# a way to find the larges number
# convert input from string ()
# is it a positive number (no)
# can the user add more than one number ()
# if an input force to an integer ()


# 3. Execute
def calc_largest():
    # TODO
    pass
# 4. Reflect and repeat previous steps
Ilgar Ilyasov 10:23 PM
https://github.com/LambdaSchool/Intro-Python-II
LambdaSchool/Intro-Python-II
Second part of introduction to Python basics
Stars   
#
Types of requirements
1. Business requirements
    .define the overall project objectives and 
    what the stakeholder is trying to solve
    with their idea
2. User Requirements
    .Describe user expectations and how they will 
    interact with the product
    .user scenarios often outline the tasks your 
    users want to complete with the product.
3. Functional Requirements
    .Provide specifics on how a produc should 
    behave and specify the development needs

Rock paper scissors game

requirements 
    2 players
        .one human users
        .one computer player that the human competes against
    Each player has 3 choices:
        .rock
        .paper
        .scissors
    there are three results after both the human
    and the computer make one of their choices:
       win
       lose
       tie
    the rules for figuring out who wins and who loses are:
        rock beats scissors
        paper beats rock
        scissors beats paper
    a tie occurs if both users shoes the same option

UPER
    understand
        1. how to start the game
        2. how to input answers
        3. how does computer make choices
        4. how to display options
        5. how to display score
        6. how to save scores (possible persistent data)
        7. how to update saved scores
        8. how to set rules
        9. how to end game
    plan
        1.
        2.
        3.
    execute
    reflect

#
Keyword argument 
    an argument that has an identifier before it
    identifier
        complex(real=4, imag=2)
        complex(**{'real': 4, 'imag': 2})
Positional Arguments
    an argument w/o a keyword argument
        complex(4, 2)
        complex(*(4,2))
Argument are assigned to    

    example: addition

    def f1(a,b):
        return a + b

    print("a + b = ",(f1(1,2)))
#

#

args and kwargs in Python

the special syntax *args in function definitions in python 
is used to pass a variable number of arguments to a function.
It is used to pass a non-keyworded, variable


def addUp(*add):
    for num in add
        print(add)
    addUp(1)
    addUp(1,2,3)


arbitrary argument-

def f2(*add):
    if len(add) == 1:
        return add[0]
    else:
        return add[-1] + f2(*add[:-1])
print(f2(1))                    # Should print 1
print(f2(3, 3))                 # Should print 6
print((f2(2, 4, -18)))          # Should print -12
print(f2(7, 9, 1, 5, 4, 4, 0))  # Should print 30

#Testing
def concat(*args, sep=" /"):
    return sep.join(args)
concate('Hey', 'hoe', 'hi', 'hoe')


Defaul arguments in Python

Python allows function args to have default values.
If the functionis called withou the argument, the argument gets
its default value.

Default Arguments:
Python hass a differernt way of representing 
syntax and default values for function arugments. Default values
indicate that the function arugment will take value if nonlocal
argument value is passed during function call. the default value is 
assigned by using assignment(=) operator of the form keywordname=value

def student(firsname, lastname="Jones", standard='Fith'):
    print(firstname, lasname, 'studies in', standard, 'Standard')


11. Keyword Arguments
https://treyhunner.com/2018/04/keyword-arguments-in-python/

12. scopes


13. reading and writing files
    .open() returns a file object   
        most common w/2 arguments:
        open(filename, mode).close
    f = open('schoolfile', 'w')

    'w': write only(existing,file w/same name file will erease)
    'a': opens file for append; any data written to the file is automatically added to the end.
    'b': this mode should be used for all files that dont contain text.
    "r" Opens a file for reading only.
    'r+': opens file for both reading and writing 
    "rb" Opens a file for reading only in binary format.
    "rb+" Opens a file for both reading and writing in binary format.

    with open('schoolfile',) as f:
        read_data = f.ready()

#we can also check the file has been closed by automatically closed.
        f.closed
    
    if not using with, use
    f.close()
    

Writing files

Python III - OOP 

    Object Oriented Programming: Allows use to model real world/abstrect concepts as objects and find relationships between objects

class [nount] aka [playe]

class: two main parts
        attributes [adjectives] = health, strength
        methonds [verbs] = run, jump, use an item

animals -> [name, diet] -> method[move(), eat()]

programming paradigm aka OOP


class Animal:
    ""A simple example class""
    define class

implement a constructor
        special type of method
        gives attriburtes their initial value
        init() in python

    class Animal:
        def_init(name,hunger, diet):
            self.name = name
            self.hunber = hunger
            self.diet = diet
        
    method

    one or more lines of code
    defines a specific behavior or action
    may return a value

class Animal:
    ""A simple example class""
    def_init(name, hunber, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and hunber < 25:
            hunger +=food

***self refers to the class-level attribute(name)

Summary
Classes [nouns] are used to model real world objects

Thiknk of them as blueprints to make multiple instance of the same object

They contain:
    .attributes[adjectives]
    .methods[verbs]

Funcitonal vs Object Oriented programming:

Function is stateless
Object Oriented is for persistent state management for saving data.


# dedicated separate file for main

player
def __init__(self, ..., room)


room
    def __init__(self., ..., name, description):
        ...
        self.name = name
        self.description = description

Python IV
is-a
    parent/child
    type/sub-type

    more general parent class is created to define
    shared attributes & behaviors

    more specific child class is used for 
    unique details


Restaurant Management System

Employee

inhertiance 

Association
has-a is a link btw two classes

Composition
    class A CANNOT exist class B

Aggregation
    class A CAN exist independently of class B


    Restaurant  <---- Menu 

    Employee


    chef waiter

has-a


class Restaurant:
    def __init__(self, name, dinner_menu):
 "has a"       self.name = name
 "has a"       self.dinner_menu = dinner_menu

class Food:
    def __init__(self, name, is_vegetarian=False):
        self.name = name
        self.is_vegetarian = is_vegetarian

class Menu: 
     def __init__(self, name, dinner_menu):
         self.name
         self.dinner_menu
         self.dishes = Food[]
         self.drinks = Drink[]

# ***CREATELY*** https://app.creately.com/

Store
________________________
name
categories: list
________________________
+ __str__(self): String
+ __get_name__(self):String
+ __set_name__(self, new_name):None

Category
________________________
- name: String
________________________
+ __str__(self):String


Item
________________________
-category: Category
-id: int
-name: String
-price: float
-in_stock: bool
_________________________
-Restock(): bool
.get__():Type
.set__():Type
.sold():TypeError
-__str__():String



Milk  #connects to Item
-type:String
-expiration_date: TypeError
__________________________
+__init__():TypeError
+getters/setters

Ice Cream
__________________________
flavor: String
size: int
__________________________
melt(args): type
