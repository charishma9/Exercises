# Code your solution here
from provided_code import grades

letter_grades =[]
for x in grades:
    if 90<=x<=100:
        letter_grades.append('A')
    elif 70<=x<=89:
        letter_grades.append('B')
    elif 50<=x<=69:
        letter_grades.append('C')
    elif 35<=x<=49:
        letter_grades.append('D')
    else:
        letter_grades.append('F')
