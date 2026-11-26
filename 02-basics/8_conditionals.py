# ==========================================
# 1. conditionals
# ==========================================

# if statement
x = 10
if x > 20:
    print(True)

if len("chars") > len("char"):
    print(True)


# elif statement
weather = int(input("Enter temparature : "))
if 10 <= weather <= 20:
    print("cool")
elif 21 <= weather <= 30:
    print("cloudy")
elif 31 <= weather <= 40:
    print("sunny")


# if-elif-else
marks = int(input("Enter your marks : "))
if 90 <= marks <= 100:
    print("O")
elif 80 <= marks <= 89:
    print("AA")
elif 70 <= marks <= 79:
    print("A")
elif 60 <= marks <= 69:
    print("B")
else:
    print("C")


# nested if statement 
x = 10
if x > 0:
    if x %2 == 0:
        if not(x%2 != 0):
            print(x)