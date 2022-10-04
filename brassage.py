
# Generer les cartes :
carte1 = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
carte2 = ["♥","♦","♣","♠"]
liste_cartes = []
for i in carte2:
    for j in carte1:
         liste_cartes.append(str(j+i))

# print(liste_cartes)


"""liste_cartes = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
                "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
                "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
                "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]"""


# Afficher les cartes sur 4 lignes de 13 elemenets:
def Affichage(liste_cartes):
    for i in range(0,len(liste_cartes),13):
        print("  ".join(liste_cartes[i: i+13]))

# Brasser les carte en divisant l'ensemble en 2:

def Melange_Carte(liste_cartes):
    moitie = len(liste_cartes) // 2
    premier_partie = (liste_cartes[moitie:])
    deuxieme_partie = (liste_cartes[:moitie])

    liste_brasser = []
    for i in range(moitie):
        liste_brasser.append(premier_partie[i])
        liste_brasser.append(deuxieme_partie[i])

    """Autre maniere que avant: C'est que on va commencer de depart et de la moitie en meme temps
    for i in range(moitie_deck):
        nouveau_paquet.extend([cartes[i], cartes[i + moitie_deck]])"""

    return liste_brasser

# Sauvegarder le resultat de brassage dans un fichier .txt avec la format adequate:
def Sauvegarder(cartes):
    f = open("cards.txt", "w",encoding="utf-8", errors="ignore")
    cartes_str =""
    for i in range(4):
        for carte in cartes[i * len(cartes)//4:(i+1) * len(cartes)//4]:
            cartes_str += carte + " "

        cartes_str += "\n"
    f.write(cartes_str)
    f.close()

# Creation d'un menu:
def main():
    condition= True
    while condition:
        menu = int(input("1- Afficher l'état du jeu de carte \n2- Effectuer un brassage inter-coupé \n3- Sauvegarder l'état final dans un fichier .txt\nChoisissez votre option : "))
        if menu == 1:
            Affichage(liste_cartes)
        elif menu == 2:
            cartes = Melange_Carte(liste_cartes)
        elif menu == 3:
            Sauvegarder(cartes)
            print("\n FIN DE PROGRAMME \n")
            condition = False
        else:
            print("Choix invalide")
main()



