# ==========================
# Type Casting & Type Conversion
# ==========================

# Type Casting
"""
There are two types of type casting ->
    - Implicit Type Casting
    - Explicit Type Casting
"""

''' Implicit Type Casting '''
num1 = 12
num2 = 12.0

result1 = num1 + num2
print(result1)


''' Explicit Type Casting '''
print(int(result1))


# Type Conversion
# int to str
num = 12
print(str(num))

# str to int
text = "12"
print(int(text))

# error -> ValueError: invalid literal for int() with base 10: 'ar'
text2 = "ar"
print(int(text2))

# int to float
num = 12
print(float(num))

# float to int
num2 = 12.190
print(int(num2))