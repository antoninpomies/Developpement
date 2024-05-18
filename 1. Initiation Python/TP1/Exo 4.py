saisie = input("Entrez chaine : ")
for caractere in saisie:
    valeur = ord(caractere)
    valeurHexa = format(valeur, 'x')
    valeurBin = format(valeur, 'b')

    print("===Caractère : ", caractere, "===")
    print("/ En décimal : ", valeur)
    print("/ En Hexadecimal : ", valeurHexa)
    print("/ En Binaire", valeurBin)
    print("=====================")