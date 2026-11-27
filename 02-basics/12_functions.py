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