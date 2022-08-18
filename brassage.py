#Évite d'écrire les 52 cartes manuellement, génère ton paquet de manière dynamique
#Ca évite les erreurs, par exemple il te manque un trois pour les trèfles
liste_cartes = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
                "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
                "A♣","2♣","♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
                "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
#print(len(liste_cartes))

#Solution intelligente
def Affichage(liste_cartes):
    for i in range(0,len(liste_cartes),13):
        print(" ".join(liste_cartes[i: i+13]))

#Bonne utilisation des tranches, très bien
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
            #Fonctionne mais faudrait ajouter un espace entre les cartes
            cartes_str += carte #+ " "
        cartes_str += "\n"
    f.write(cartes_str)
    f.close()

	
print("1- Afficher l'état du jeu de carte \n2- Effectuer un brassage inter-coupé \n3- Sauvegarder l'état final dans un fichier .txt")
menu = True
while menu:
    #Place ton print ici pour éviter d'avoir à l'écrire à 2 endroits.
    menu = int(input("Choisissez votre option : "))
    if menu == 1:
        Affichage(liste_cartes)
    elif menu == 2:
        #il y avait un s de trop à liste, je l'ai enlevé
        liste_cartes = Melange_Carte(liste_cartes)
    elif menu == 3:
        Sauvegarder(liste_cartes)
        print("\n FIN DE PROGRAMME \n")
        #Utilises menu = false au lieu de forcer la sortie
        exit()
    
    print("1- Afficher l'état du jeu de carte \n2- Effectuer un brassage inter-coupé \n3- Sauvegarder l'état final dans un fichier .txt")

