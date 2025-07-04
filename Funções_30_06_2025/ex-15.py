def analisa_lista(lista):
    nlista=sorted(lista)
    mai= nlista[-1]
    men=nlista[0]
    med=sum(lista)/ len(lista)
    return mai, men,med

teste=[2,3,7,4,8,3,1,9]

print("O maior número, O menor numero e a média da lista é respectivamente:",analisa_lista(teste))