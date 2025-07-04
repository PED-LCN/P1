def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

l1=[1,2,3]
l2=['a','b','c']
print(intercalar_listas(l1,l2))