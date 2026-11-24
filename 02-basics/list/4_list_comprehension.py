# ==========================================
# 1. List comprehension
# ==========================================

nums = [i for i in range(0, 11)]
print(nums)

even = [i for i in range(1, 21) if i%2 == 0]
print(even)

odd = [i for i in range(1, 21) if not(i%2==0)]
print(odd)