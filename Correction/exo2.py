#!/usr/bin/python3

valeur_defaut = '1234567890123'
saisie = input("Donnez vote numéro SS [%s]" % valeur_defaut)
valeur = saisie or valeur_defaut
numero_ss = valeur

valeur_defaut = '11'
saisie = input("Donnez vote clé de vérification SS [%s]" % valeur_defaut)
valeur = saisie or valeur_defaut
cle = valeur

sexe = numero_ss[0]
annee_naissance = numero_ss[1:3]
mois_naissance = numero_ss[3:5]
dpt_naissance = numero_ss[5:7]
commune_naissance = numero_ss[7:10]
ordre_naissance = numero_ss[10:]

print('Sexe :', sexe)
print('annee_naissance :', annee_naissance)

cle_verifiee = 97 - (int(numero_ss) % 97)

if (int(cle) == cle_verifiee):
    print("Vérification OK !")
else:
    print("Erreur code/clé")
