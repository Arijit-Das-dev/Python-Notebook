# ==========================================
# 1. functions
# ==========================================
"""
Why we need a function ?
- To make code modular
- Improves readability
- Improves efficiency
- We dont have to write a task again and again if we use functions.

Function naming rules:
    - must start with a letter or underscore -> function(), _function()
    - can only contain letter, number or underscore.
    - functions are case-sensitive,
        - myFunction() and myfunction() is different.
"""

# ==================================================================================================================================== #

# basic syntax
def greet():
    return "good morning"
print(greet())


# example 1
def to_celcius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius
print(to_celcius(temp=77))


# example 2
def send_message(msg):
    return f"message : {msg}"

message = send_message(msg="hi, this is alex")
print(message)


# ==================================================================================================================================== #

""" functions with arguements """
# -> parameters
# -> arguements

# example 1
def say_hello(name):            # <- variable inside first bracket is called -> parameter
    return f"hello {name}"

names = ["John", "Alex"]
for name in names:
    print(say_hello(name=name)) # The value we are passing is called arguements

""" There are two types of arguements are present """
# -> keyword arguements
# -> positional arguements


# keyword arguements
# order of arguements can be any order
def myFunction(name, email):
    return f"{name}, {email}"
print(myFunction(name="Alex", email="alex@gmail.com"))


# positional arguements
# order of arguments should be in correct order
print(myFunction("Alex", "alex@gmail.com"))


# mixing positional and keyword arguements
# positional arguements must come before keyword arguements
def add(a, b):
    return a+b

addition = add(13, b=12)
print(addition)


# passing different data types
# List
def show_items() -> list:
    fruits = ["apple", "banana"]
    return fruits
items = show_items()
print(items[0])
print(items[1])


# dictionary
from typing import Any
def mapping(details) -> dict[str, Any]:
    
    for keys in details:
        print(keys, ":" ,details[keys])

user_profile = {
    "user_id": 1042,
    "username": "Alex",
    "full_name": "Alex",
    "age": 27,
    "email": "Alex@example.com",
    "city": "London",
    "is_active": True,
    "account_balance": 4500.75,
    "roles": ["admin", "editor"],
    "last_login": "2026-11-26"
}
mapping(user_profile)


# positional-only arguements
"""
positional arguements - def func(val, /)
keyword arguements - def func(*, val)

"""

def my_tool(tools, /):
    for key, value in tools.items():
        print(f"{key} : {value}")

tools = {
    1:"get_weather",
    2:"Get_news",
    3:"get_data"
}
# you can not use 
my_tool(tools)


# keyword-only arguements
def subtract(*,a, b):
    return a-b

sub = subtract(a=2, b=5)
print(sub)


# ==================================================================================================================================== #

"""
*args
**kargs
"""

# *args
# example 1
def example(*args):
    return args
# *args returns tuple ()
print(type(example("alex", 1, 12)))


# example 2
def greet(*names):
    for name in names:
        print("hello", name)
greet("alex", "arijit")


# example 3
def add(*nums):
    summ = 0
    for i in range(0, len(nums)):
        summ = summ + nums[i]
    return summ
print(add(1, 2, 3, 4))


# **kwargs
def my_function(**kargs):
    for key, value in kargs.items():
        print(key, value)

# kwargs returns dictionary
my_function(name = "Arijit", ids = 1, sec = "A")


# ==================================================================================================================================== #

"""
function scope
"""

# variable created inside a function is called local scope
def local_scope():
    x = 100
    return x
print(local_scope())


# variable created outside of the function is called global scope
y = 50
def global_scope():
    return y
print(global_scope())


# if you change the same variable value inside and outside of the function , it will treat them as two seperate value
z = 10
def example():
    z = 20
    return z
print(z)
print(example())