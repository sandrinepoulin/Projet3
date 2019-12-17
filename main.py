'''Ce module traite les fonctions qui ne communiquent pas avec le serveur par le module request'''

import argparse
import api

def analyser_commande():
    '''Cette fonction permet de traiter la ligne de commande'''
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 3')
    parser.add_argument(metavar='idul', dest='idul',
                        help='IDUL du joueur.')
    parser.add_argument('-a', '--automatique', action='store_true', default=False, help='Activer le mode automatique.')
    parser.add_argument('-x', '--graphique', action='store_true', default=False, help='Activer le mode graphique.')
    '''group.add_argument('-ax', action='store_true', default=False)'''
    args = parser.parse_args()

    if args.a:
        # définir comment jouer automatique, le joueur 2 est le serveur et nous on fait une boucle avec jouer_coup
        pass
    elif args.x:
        # définir comment jouer avec l'interface graphique --> appeler QuoridorX
        pass
    else:
        # jouer manuellement avec le damier ascii
        pass
    return args.idul

analyser_commande()
'''Pout faire des tests avec le terminal
L'idul s'appelle args.idul (quand on va l'utiliser)'''


'''J'ai enlevé la valeur par défaut du pemier argument (pour l'idul)
puisque ça ne servait à rien (comme c'est un argument obligatoire)
On a les bons arguments!! reste juste à mettre les bonnes actions dans les if, en fonction des classes que nous allons définir'''

