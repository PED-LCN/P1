def  fatorial(n):
    m=1
    for i in range(1,n+1):
        fat=m*i
        m=fat
    return m

k=6
print(fatorial(k))