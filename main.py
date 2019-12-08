'''Ce module traite les fonctions qui ne communiquent pas avec le serveur par le module request'''

import argparse
import api

def analyser_commande():
    '''Cette fonction permet de traiter la ligne de commande'''
    parser = argparse.ArgumentParser(description='Jeu Quoridor - Phase 1')
    parser.add_argument(metavar='idul', default='idul du joueur', dest='idul',
                        help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', dest='accumulate', action='store_const',
                        const=sum, default=False,
                        help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args
