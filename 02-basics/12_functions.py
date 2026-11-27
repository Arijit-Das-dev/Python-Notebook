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


def to_celcius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius
print(to_celcius(temp=77))


def send_message(msg):
    return f"message : {msg}"

message = send_message(msg="hi, this is alex")
print(message)


# ==================================================================================================================================== #
""" functions with arguements """
# -> parameters
# -> arguements

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

