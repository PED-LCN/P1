def palindrome(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
print("TESTADOR PALINDROMO")
print("-------------------")
P=input("Digite uma palavra: ")
print(palindrome(P))  