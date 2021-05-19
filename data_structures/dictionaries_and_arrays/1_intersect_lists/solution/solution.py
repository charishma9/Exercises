def intersect_lists(lst1,lst2):
    lst = []
    for i in lst1:
        if i in lst2:
            lst.append(i)
    return lst
