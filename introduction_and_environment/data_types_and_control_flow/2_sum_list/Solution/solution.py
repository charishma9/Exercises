from provided_code import lst
# Code your solution here
total = 0
for i in range(len(lst)):
    if type(lst[i]) == int:
        total = total + lst[i]

