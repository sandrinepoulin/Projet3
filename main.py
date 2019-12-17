'''Ce module traite les fonctions qui ne communiquent pas avec le serveur par le module request'''

import argparse
import api
import quoridor
import quoridorx

def analyser_commande():
    '''Cette fonction permet de traiter la ligne de commande'''
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 3')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument(metavar='idul', dest='idul',
                        help='IDUL du joueur.')
    group.add_argument('-a', '--automatique', action='store_true', default=False, help='Activer le mode automatique.')
    group.add_argument('-x', '--graphique', action='store_true', default=False, help='Activer le mode graphique.')
    group.add_argument('-ax', '--graphique_automatique', action='store_true', default=False, help='Activer le mode automatique et graphique.')

    args = parser.parse_args()

    if args.automatique:
        idul = analyser_commande().idul
        dico = api.débuter_partie(idul)
        Id = dico['id']
        jeu = quoridor.Quoridor(dico)
        while quoridor.QuoridorError False:
            jeu.jouer_coup(1)
            dico = api.jouer_coup(Id, type_de_coup, position)
        print(jeu)

    elif args.graphique:
        idul = analyser_commande().idul
        dico = api.débuter_partie(idul)
        jeu = quoridorx.QuoridorX(dico)
        Id = dico['id']
        i = True
        while i:
            coup = input("Choisir un coup (déplacement = D, mur horizontal = MH, mur vertical = MV) et presser la touche ⏎: ")
            if coup == 'D':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
            elif coup == 'MH':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
            elif coup == 'MV':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
        jeu.afficher()

    elif args.graphique_automatique:
        idul = analyser_commande().idul
        dico = api.débuter_partie(idul)
        Id = dico['id']
        jeu = quoridorx.QuoridorX(dico)
        while quoridor.QuoridorError False:
            jeu.jouer_coup(1)
            dico = api.jouer_coup(Id, type_de_coup, position)
        jeu.afficher()

    else:
        jeu = quoridor.Quoridor(dico)
        idul = analyser_commande().idul
        dico = api.débuter_partie(idul)
        Id = dico['id']
        i = True
        while i:
            coup = input("Choisir un coup (déplacement = D, mur horizontal = MH, mur vertical = MV) et presser la touche ⏎: ")
            if coup == 'D':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
            elif coup == 'MH':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
            elif coup == 'MV':
                position = input("Préciser la position (x, y) et presser la touche ⏎: ")
                dico = api.jouer_coup(Id, coup, position)
        print(jeu)

    return args.idul

analyser_commande()
