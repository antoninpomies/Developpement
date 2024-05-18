#!/usr/bin/python3

# version complète
# saisie = input("Donnez une valeur entière :")
# valeur = int(saisie)

# version compacte
# valeur = int(input("Donnez une valeur entière :"))

# version script
valeur_defaut = 10
saisie = input("Donnez une valeur entière [%d]" % valeur_defaut)
# if not saisie:
#     valeur = valeur_defaut
# else:
#     valeur = int(saisie)
saisie = saisie or valeur_defaut
valeur = int(saisie)

print(valeur)

#for (i=0; i< valeur; i++)
# for v in range(0,valeur):
#     print('*', end='')

print('*' * valeur)
