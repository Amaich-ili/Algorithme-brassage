
# Étape 1

liste_cartes = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
                "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
                "A♣","2♣","♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
                "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
#print(len(liste_cartes))

# Étape 2
def Affichage(liste_cartes):
    for i in range(0,len(liste_cartes),13):
        print(" ".join(liste_cartes[i: i+13]))


from asyncore import read
import random
def Melange_Carte(liste_cartes):
    liste_carte_melange = random.sample(liste_cartes,52)
    return(Affichage(liste_carte_melange))


from asyncore import read
def Sauvegarder():
    with open("resultat.txt", "r") as fichier:
        print(fichier.read())
        #fichier.write(Melange_Carte())
	
   
menu = True
while menu:
    menu = int(input("Choisissez votre option : "))
    if menu == 1:
        Affichage(liste_cartes)
    if menu == 2:
        Melange_Carte(liste_cartes)
    if menu == 3:
        Sauvegarder()
        exit()
    print("1- Afficher l'état du jeu de carte \n2- Effectuer un brassage inter-coupé \n3- Sauvegarder l'état final dans un fichier .txt")

print("\nFIN DE PROGRAMME")