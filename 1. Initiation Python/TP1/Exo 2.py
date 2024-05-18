#======Deuxième Exo======
numSecu = input("Saisissez votre numéro de sécu : [Entée pour defaut]")
cleVerif = input("Saisissez votre clé de vérification : [Entée pour defaut 64]")
numSecuDefaut, cleVerifDefaut = "1234567891234", "64"
numSecu = numSecu or numSecuDefaut
cleVerif = cleVerif or cleVerifDefaut
decompSecu = [int(a) for a in str(numSecu)]
numDecomp = numSecu[0:1] + ' ' + numSecu[1:3] + ' ' + numSecu[3:5] + ' ' +  numSecu[5:7] + ' ' +  numSecu[7:10] + ' ' + numSecu[10:13]
print ("Votre Numéro est : ", end="")
print (numDecomp)
print ("Votre Clé est : ", end="")
print (cleVerif)
calculVerif = 97 - (int(numSecu) % 97)
if (int(cleVerif) == int(calculVerif)):
    print("La clé est correcte")
else:
    print("La clé n'est pas correcte")