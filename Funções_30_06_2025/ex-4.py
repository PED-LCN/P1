def media(a,b,c):
    m = a +b + c
    return m/3

def requisição():
    a=int(input("Digite um número:"))
    return a 

n1= requisição()
n2= requisição()
n3 = requisição()

print("A media dos números é: ",media(n1,n2,n3))
