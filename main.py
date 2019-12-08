'''Ce module traite les fonctions qui ne communiquent pas avec le serveur par le module request'''

import argparse
import api

def analyser_commande():
    '''Cette fonction permet de traiter la ligne de commande'''
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    group = parser.add_mutually_exclusive_group() 
    parser.add_argument(metavar='idul', dest='idul',
                        help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', action='store_true',
                        help='Lister les identifiants de vos 20 dernières parties.')
    group.add_argument('-a', action='store_true', default=False)
    group.add_argument('-x', action='store_true', default=False)
    group.add_argument('-ax', action='store_true', default=False)
    args = parser.parse_args()

    if args.a:
        # définir comment jouer automatique
        pass
    elif args.x:
        # définir comment jouer avec l'interface graphique
        pass
    elif args.ax:
        # définir comment jouer automatique avec l'interface graphique
        pass
    else:
        # jouer manuellement  avec la damier ascii
        pass
    return args.idul

'''analyser_commande()
Pout faire des tests avec le terminal'''


'''J'ai enlevé la valeur par défaut du pemier argument (pour l'idul)
puisque ça ne servait à rien (comme c'est un argument obligatoire)
On a les bons arguments!! reste juste à mettre les bonnes actions dans les if, en fonction des classes que nous allons définir'''

