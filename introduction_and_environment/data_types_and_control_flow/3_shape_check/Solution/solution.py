# Code your solution here
dict = {3:'Triangle',4:'Quadrilateral',5:'Pentagon',6:'Hexagon',7:'Heptagon',8:'Octagon',9:'Nonagon'}
g_lst=[]
while True:
    g_int = int(input())
    if 3<=g_int<=9:
        g_lst.append(dict.get(g_int))
    else:
        False




          