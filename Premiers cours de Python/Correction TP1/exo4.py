#!/usr/bin/python3

saisie = input("Entrez chaine :")

for caractère in saisie:
    valeur = ord(caractère)
    valeur_hexa = format(valeur, 'x')
    valeur_bin = format(valeur, 'b')

    # print(format(valeur,'x'))
    print("Caractère :", caractère)
    print("Valeur decimal: ", valeur)
    print("Valeur hexa: ", valeur_hexa)
    print("Valeur binaire: ", valeur_bin)
    print()
