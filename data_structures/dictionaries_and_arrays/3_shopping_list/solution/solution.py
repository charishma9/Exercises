def cheapest_store(grocery_dict,shopping_list):
    wal ={}
    for k,v in grocery_dict.items():
        #print(k)
        s =0
        for i in shopping_list:
            if i in v:
                #print("yes",v[i])
                s = s+v[i]
            else:
                #print("No",i)
                s = s+5
        #print("sum",s)
        wal[k]=s
        #print(sorted(wal))
    store = min(sorted(wal.keys()),key=(lambda k: wal[k]))
    return store

