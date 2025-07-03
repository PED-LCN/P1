def maior_numero(a,b,c):
    if a > b and a>c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
n=5
m=10
k=8
print (maior_numero(n,m,k))  