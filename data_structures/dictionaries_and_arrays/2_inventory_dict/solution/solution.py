def inventory_price(idict):
    pr_list = []
    for k,v in idict.items():
        pr_list.append(v[0]*v[1])
    
    return sum(pr_list)