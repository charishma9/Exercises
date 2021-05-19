def student_grades(sgrades,letter_grades):
    result = {}
    grade = {}
    for (i,j),(l,m) in zip(sgrades.items(),letter_grades.items()):
        marks = sgrades.get(i)
        avg =round(sum(marks)/len(marks))
        result[i] = avg
        print(result)
        if avg >90:
            grade[i] = ("A",avg)
        elif 75<avg<89:
            grade[i]=("B",avg)
        elif 60<avg<74:
            grade[i] = ("C",avg)
        elif 45<avg<59:
            grade[i] = ("D",avg)
        elif 30<avg<44:
            grade[i] =("E",avg)
        else:
            grade[i] = ("F",avg)
    return grade
    


