def senha_segura(passw):
    maisc=any(char.isupper() for char in passw)
    minus=any(char.islower() for char in passw)
    numb=any(char.isdigit() for char in passw)
    if len(passw)>=8 and maisc==True and minus==True and numb == True :
        return True
    else:
        return False
    
senha_teste=input("Digite uma senha: ")
print(senha_segura(senha_teste))

