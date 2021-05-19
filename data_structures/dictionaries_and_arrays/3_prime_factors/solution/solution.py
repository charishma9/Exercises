def prime_factors(n):
    fac =[]
    for i in range(1,n + 1):
        if n % i == 0:
            count = 1
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                fac.append(i)
    return fac
            
    