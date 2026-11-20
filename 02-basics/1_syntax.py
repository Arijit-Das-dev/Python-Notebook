# ==========================================
# 1. COMMENTS & INDENTATION
# ==========================================
# Single-line comments start with '#'.
# Python uses indentation (typically 4 spaces) to define code blocks instead of {}.

x = 10
y = 5

if x > y:
    print("x is greater than y")  # Indented block inside 'if'
    if x == 10:
        print("x is specifically 10")  # Nested block uses further indentation


# ==========================================
# 2. VARIABLES & BASIC DATA TYPES
# ==========================================
# Variables are created upon assignment; no explicit declaration keyword is needed.
name = "Ada"              # str (string)
age = 28                  # int (integer)
height_m = 1.68           # float (floating-point number)
is_developer = True       # bool (boolean: True or False)
nothing_yet = None        # NoneType (represents absence of value)

# String formatting (f-strings)
greeting = f"Hello, {name}! Age: {age}, Height: {height_m}m"
print(greeting)


# ==========================================
# 3. OPERATORS & CONDITIONALS (if / elif / else)
# ==========================================
score = 84

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Score {score} -> Grade {grade}")

# Logical operators: and, or, not
has_id = True
has_ticket = False
can_enter = has_id and (has_ticket or score >= 80)
print(f"Can enter: {can_enter}")


# ==========================================
# 4. DATA STRUCTURES: LISTS, TUPLES, DICTS, SETS
# ==========================================
# List: ordered, mutable (changeable), allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print("First fruit:", fruits[0])

# Tuple: ordered, immutable (cannot be changed after creation)
coordinates = (22.5726, 88.3639)
lat, lon = coordinates  # Tuple unpacking
print(f"Lat: {lat}, Lon: {lon}")

# Dictionary: key-value pairs, mutable
user = {
    "username": "ada_l",
    "role": "admin",
    "active": True,
}
user["active"] = False
print("User role:", user.get("role"))

# Set: unordered collection of unique items
unique_tags = {"python", "syntax", "python", "basics"}
print("Unique tags:", unique_tags)


# ==========================================
# 5. LOOPS & COMPREHENSIONS
# ==========================================
# 'for' loop over a sequence or range()
print("Counting 0 to 2:")
for i in range(3):
    print(f"  i = {i}")

# 'while' loop runs while condition is True
countdown = 3
while countdown > 0:
    print(f"  Countdown: {countdown}")
    countdown -= 1

# List comprehension: concise way to build lists
squares = [n ** 2 for n in range(1, 6)]
print("Squares 1..5:", squares)


# ==========================================
# 6. FUNCTIONS & DEFAULT / KEYWORD ARGUMENTS
# ==========================================
def calculate_total(price: float, tax_rate: float = 0.18, discount: float = 0.0) -> float:
    """Return final price after discount and tax."""
    discounted = price - discount
    return round(discounted * (1 + tax_rate), 2)

final_amount = calculate_total(price=1000.0, discount=100.0)
print(f"Final amount: {final_amount}")


# ==========================================
# 7. ERROR HANDLING (try / except)
# ==========================================
raw_input_val = "42"

try:
    parsed = int(raw_input_val)
    result = 100 / parsed
    print(f"100 / {parsed} = {result:.2f}")
except ValueError:
    print("Could not convert input to an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Cleanup/final check complete.")