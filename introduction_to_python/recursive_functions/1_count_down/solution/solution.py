def count_down_from(num):
    if num == 1:
        return num
    else:
        print(num)
        return count_down_from(num-1)
        
        