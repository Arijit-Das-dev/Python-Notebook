# ==========================================
# 1. match case
# ==========================================


# example 1
marks = int(input("Enter your marks : "))

match marks:
    case m if m >= 90 and m <= 100:
        print("Grade O")
    case m if m >= 80 and m <= 89:
        print("Grade AA")
    case m if m >= 70 and m <= 79:
        print("Grade A+")
    case m if m >= 60 and m <= 69:
        print("Grade B")
    case m if m >= 50 and m <= 59:
        print("Grade C")
    case m if m >= 40 and m <= 49:
        print("Grade D")
    case _:
        print("Failed , better luck next time !")

# example 2
day = int(input("Enter day : "))

match day:
    case d if d >= 6 and d <= 7:
        print("Week off")
    case d if d >= 1 and d <= 5:
        print("week day")
    case _:
        print("Invalid day!")