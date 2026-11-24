# ==========================
# Operator
# ==========================


# Arithmatic Operators
"""
+   addition
-   subtraction
*   multiplication
/   division
//  floored divison
%   reminder
"""
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)


# Comparison Operators
"""
==
>
<
>=
<=
!=
"""
print(a==b)
print(a>b)
print(a<b)
print(a!=b)
print(a>=b)
print(a<=b)

# Assignment Operators
"""
=
+=
-=
*=
/=
//=
"""
a += 10
print(a)
b -= 5
print(b)
a //= 2
print(a)
b /= a
print(b)


# Membership Operators
"""
in
not in
"""
text = "Hi, this is John"
print("John" in text)
print("Alex" not in text)


# Logical Operators
"""
and 
or 
not
"""
print(a>b and b<a)
print(a>b or b>a)

if not(a<b):
    print("True")


# Identity Operators
"""
is 
is not
"""
a = [1, 2]
b = [1, 2]

print(a is b)
print(a is not b)