def eh_pah(n):
    if n%2 == 0:
        return True
    else:
        return False
    
n= int(input("digite um numero: "))
if eh_pah(n) == True:
    print("o numero é par")
else:
    print("o numero é impar")