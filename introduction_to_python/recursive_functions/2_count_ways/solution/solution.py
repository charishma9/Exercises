def count_ways(steps):
    return step(steps+1)

def step(m):
    if m<=1:
        return m
    return step(m-1)+step(m-2)
