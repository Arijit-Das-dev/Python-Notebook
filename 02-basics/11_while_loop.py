# ==========================================
# 1. while loop
# ==========================================

# simple syntax
i = 0
while i <= 10:
    print(i)
    i+=1

# break statement
i = 0
while i <= 10:
    if i == 5:
        break
    print(i)
    i+=1

# continue statement
i = 0
while i <= 10:
    if i == 5:
        continue
    print(i)
    i+=1