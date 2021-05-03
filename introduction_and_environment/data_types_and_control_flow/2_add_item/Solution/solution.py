from provided_code import d
# Code your solution here
for i in range(1,6):
    ispresent = i in d
    if ispresent == False:
        d[i] = "found it!"



