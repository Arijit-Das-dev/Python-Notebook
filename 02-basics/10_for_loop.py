# ==========================================
# 1. for loop
# ==========================================
""" 
i = index number
range = helps to iterate numbers within a given range

        range(start, stop, step)

        start = starting number 
        stop = ending number 
        step = number to skip
"""

# start = 1, stop 11
for i in range(1, 11):
    print(i)


# start = 1, stop = 11, step = 2
for j in range(1, 11, 2):
    print(j)


# iterating through list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]      <= index
 
for i in range(0, len(nums)):
    print(nums[i])

# same as using range function
for num in nums:
    print(num)


# iterating through dictionary
students = {
    "id":1,
    "name":"John",
    "dept":"BCA",
    "sec":"A",
}

# will print keys
for details in students:
    print(details)

# nested loops
for i in range(1, 11):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 5:
            print(nums[i], nums[j])