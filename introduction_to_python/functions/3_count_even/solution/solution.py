def count_even(*args):
    count = 0
    for x in args:
        if x%2==0:
            count= count+1
    return count