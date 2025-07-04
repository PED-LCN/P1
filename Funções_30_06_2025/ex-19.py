import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1,100)
    n=int(input("Dê um palpite: "))
    while n != numero_secreto:
        if n>numero_secreto:
            print("O número secreto é menor")
        elif n<numero_secreto:
            print("O número secreto é maior")
        n=int(input("Dê outro palpite: "))
    print("Parabéns, você acertou!")
    
jogo_adivinhacao()