def repetir_mensagem(a,msg):
    for i in range(a):
        print(msg)

txt= input("digite uma frase: ")
N= int(input("digite o numero de repeticoes: "))
repetir_mensagem(N,txt)