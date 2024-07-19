"""
val=0
print("valeur actuelle: " ,val)
print("Options\n1. Additionner un nombre \n2. Soustraire un nombre \n3. Multiplier par un nombre \n4. Diviser par un nombre\n5. Réinitialiser le calcul \n6. Quitter")

choix=int(input("Choisissez une option (1-6): "))
if(choix!=6):
    nbr=float(input("Entrez un nombre :"))
while choix > 0 and choix < 6 :
    if(choix==1):
        val+=nbr
        print("resutl=",val)
    elif(choix==2):
        val-=nbr
        print("resutl=", val)
    elif(choix==3):
        val*=nbr
        print("resutl=", val)
    elif(choix==4):
        if nbr!=0:
            val /= nbr
            print("resutl=", val)
        else:
            print("impossible")
    elif(choix==5):
        val =0
        print("reset=", val)
    else:
        break
    choix = int(input("Choisissez une option (1-6): "))
    if(choix!=6):
        nbr = float(input("Entrez un nombre :"))
"""

"""
import random as rand

val= rand.randint(1,100)

print("Deviner le nombre compris entre 1 et 100")
dev=int(input("Entrez votre nombre: "))
while dev !=val :
    if dev > val :
        print("Votre nombre est plus grand")
    else:
        print("Votre nombre est plus petit")
    dev = int(input("Entrez votre nombre: "))
else:
    print("Bravo vous avez trouvé !!!")
"""

"""
print("Entrez les notes de vos modules")
note=float(input("entrez la note: "))
moyenne=0
n=0
while n<6:
    if note > 20 or note < 0:
        print("veuillez entrez une note valable")
    else:
        moyenne+=note
        n += 1
    if n!=6 :
        note = float(input("entrez la note suivante: "))
moyenne/=6
print("Votre moyenne est : ", moyenne)
if moyenne < 10 :
    print("Mention: insuffisant")
elif moyenne < 12 :
    print("Mention: Passable")
elif moyenne < 14 :
    print("Mention: Assez-bien")
elif moyenne < 16 :
    print("Mention: Bien")
elif moyenne < 18 :
    print("Mention: Très-bien")
else:
    print("Mention: Excellent")
"""