# ==========================================
# 1. dictionary operations
# ==========================================


students = {
    "id":1,
    "name":"John",
    "dept":"BCA",
    "sec":"A",
}

# access items
print(students["id"])

# modify dictionary items
students["name"] = "Alex"
print(students["name"])

# delete dictionary items
del students["id"]
print(students)

# delete entire dictionary
del students

# check students dictionary is still available or not
try:
    print(students)
except NameError as n:
    print(str(n))