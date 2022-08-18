


liste_cartes = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
                "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
                "A♣","2♣","♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
                "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
#print(len(liste_cartes))


def Affichage(liste_cartes):
    for i in range(0,len(liste_cartes),13):
        print(" ".join(liste_cartes[i: i+13]))



def Melange_Carte(liste_cartes):
    liste1 = []
    liste2 = []
    moitier = len(liste_cartes) // 2
    premier_partie = (liste_cartes[moitier:])
    deuxieme_partie = (liste_cartes[:moitier])
    liste1 = premier_partie
    liste2 = deuxieme_partie

    liste_brasser = []
    for i in range(len(liste1)):
        liste_brasser.append(liste1[i])
        liste_brasser.append(liste2[i])
    return liste_brasser


def Sauvegarder(cartes):
    f = open("cards.txt", "w",encoding='utf-8', errors='ignore')
    cartes_str =""
    cartes_separee = []
    for i in range(4):
        for carte in liste_cartes[i*len(liste_cartes)//4:(i+1) * len(liste_cartes)//4]:
            cartes_str += carte
        cartes_str += "\n"
    f.write(cartes_str)
    f.close()
	
   
menu = True
while menu:
    menu = int(input("Choisissez votre option : "))
    if menu == 1:
        Affichage(liste_cartes)
    elif menu == 2:
        listes_cartes = Melange_Carte(liste_cartes)
    elif menu == 3:
        Sauvegarder(listes_cartes)
        print("\nFIN DE PROGRAMME")
        exit()
    
    print("1- Afficher l'état du jeu de carte \n2- Effectuer un brassage inter-coupé \n3- Sauvegarder l'état final dans un fichier .txt")

