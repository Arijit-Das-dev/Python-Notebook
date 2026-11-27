# ==========================
# creating variables
# ==========================
a = 12
y = "john doe"

print(a)
print(y)


# =============================
# Type of variable - check type
# =============================
print(type(a))
print(type(y))


# ==========================
# variable naming rule
# ==========================
varname = None
varName = None
var_name = None
_var_name = None
VAR_NAME = None
VARNAME = None



# ==========================
# Illegal variable names:
# ==========================
"""
- error ->

2myvar = "John"
my-var = "John"
my var = "John"

"""

# ==========================
# Multi Words Variable Names
# ==========================
# Type 1 -> Camel Case
varName = None

# Type 2 -> Pascal Case
VarName = None

# Type 3 -> Snake Case
var_name = None


# ============================
# Assigning multiple variables
# ============================
x = y = z = 10        # assigning same values to multiple variables
a, b, c = 1, 2, 3     # assigning different values to multiple variables

print(a, b, c)
print(x, y, z)