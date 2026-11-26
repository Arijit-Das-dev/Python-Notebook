# ==========================================
# 1. Loop through dictionary
# ==========================================

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

# print key value both
for key, value in user_profile.items():
    print(f"{key} : {value}")

# print only keys
for keys in user_profile:   # also can use .keys() function => user_profile.keys()
    print(keys)

# print only values
for values in user_profile.values():
    print(values)

# unpack list items inside dictionary
for values in user_profile["roles"]:
    print(values)