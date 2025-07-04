def numeros_primos (n):
    primos=[]
    for numero in range(2,n+1):
        eh_primo=True
        for i in range(2,int(numero**0.5)+1):
            if numero % i ==0:
                eh_primo=False
                break
        if eh_primo==True:
            primos.append(numero)       
    return print(primos)

numeros_primos(30)
