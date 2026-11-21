# ==========================
# string concatenation
# ==========================

hello = "Hello"
world = "world"
print(hello +" "+ world)

# error -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
num = 12
text = "A"
print(num + text) 

# fix 
print(str(num) + text)