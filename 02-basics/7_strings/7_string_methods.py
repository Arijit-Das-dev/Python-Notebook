# ==========================
# String methods 
# ==========================

text = " String methods"

print(text.upper())                     # converts to upper case
print(text.lower())                     # converts to lower case
print(text.casefold())                  # converts all the chars to lower case
print(text.startswith("S"))             # returns boolean value if startswith "S"
print(text.endswith("s"))               # returns boolean value if endswith "s"
print(text.capitalize())                # converts the first letter to Upper case
print(text.strip())                     # removes spaces from starting and ending of a string
print(text.split())                     # appends all the words in a list
print(text.rsplit())                    # returns a list of words in a text
print(text.lstrip())                    # removes spaces from the starting
print(text.rstrip())                    # removes spaces from the ending
print(text.count(" "))                  # counts specific char
print(text.find("s"))                   # finds specific char's index number
print(text.replace("String", "List"))   # replaces old word with new

print(text.islower())                   # returns True if text in lower format
print(text.isupper())                   # returns True if text in upper format
print(text.isdecimal())                 # returns True if all chars are in 0-9
print(text.isdigit())                   # returns True if all chars are digits
print(text.isalnum())                   # returns True if all characters are digits
print(text.isalpha())                   # returns True if all characters are letters (A-Z)