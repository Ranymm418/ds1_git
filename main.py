tache = []

choix = -1
while choix != 0:
    print("== Gestion des taches ==")
    print("1 - ajouter une tache")
    print("2 - afficher les taches")
    print("3 - rechercher une tache ")
    print("0 - quitter")
    choix = int(input("votre choix : "))
    if choix == 1:
        ajouter_une_tache()
    elif choix == 2:
        afficher_les_tache()
    elif choix == 3:
        rechercher_une_tache()
    elif choix == 0:
        print("fermeture du programme")
    else:
        print("choix invalide")
