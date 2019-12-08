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

def afficher_damier_ascii(dic):
    '''Cette fonction permet d'afficher correctement le damier'''
    #plaque de jeu
    nom1 = dic['état']['joueurs'][0]['nom']
    damier = ''
    pligne = f'Légende: 1 = {nom1}, 2 = automate \n' + '   ' + 35*'-' + '\n'
    for i in range(9, 0, -1):
        if i != 1:
            damier += f'{i}' +  ' | .' + 8*'   .' + ' |' '\n' + '  |' + 35* ' ' + '| \n'
        elif i == 1:
            damier += f'{i}' +  ' | .' + 8*'   .' + ' |' '\n'
    damier += '--|' + 35*'-' + '\n'
    dligne = '  | '
    for i in range(1, 10):
        if i != 9:
            dligne += f'{i}' + 3*' '
        elif i == 9:
            dligne += '9'
    damier += dligne
    damier = list(damier.splitlines())
    for i in range(len(damier)):
        damier[i] = list(damier[i])
    #placer les joueurs dans la plaque de jeu
    x1 = dic['état']["joueurs"][0]["pos"][0]
    y1 = dic['état']["joueurs"][0]["pos"][1]
    x2 = dic['état']["joueurs"][1]["pos"][0]
    y2 = dic['état']["joueurs"][1]["pos"][1]
    damier[18-2*y1][4*x1] = '1'
    damier[18-2*y2][4*x2] = '2'
    #placer les murs
    for i in range(len(dic['état']["murs"]["horizontaux"])):
        xh = dic['état']["murs"]["horizontaux"][i][0]
        yh = dic['état']["murs"]["horizontaux"][i][1]
        damier[19-2*yh][4*xh-1 : 4*xh+6] = '-------'
    for i in  range(len(dic['état']["murs"]["verticaux"])):
        xv = dic['état']["murs"]["verticaux"][i][0]
        yv = dic['état']["murs"]["verticaux"][i][1]
        damier[18-2*yv][4*xv-2] = '|'
        damier[17-2*yv][4*xv-2] = '|'
        damier[16-2*yv][4*xv-2] = '|'
    #Retransformer en String
    print(pligne + '\n'.join(''.join(i for i in ligne) for ligne in damier) + '\n')

def jouer_jeu():
    '''Cette fonction permet de jouer une partie'''
    idul = analyser_commande().idul
    dico = api.débuter_partie(idul)
    print(afficher_damier_ascii(dico))
    i = True
    while i != StopIteration:
        coup = input("Choisir un coup (déplacement = D, mur horizontal = MH, mur vertical = MV) et presser la touche ⏎: ")
        if coup == 'D':
            position = input("Préciser la position (x, y) et presser la touche ⏎: ")
            dico['état']["joueurs"][0]["pos"] = position
            api.jouer_coup(dico['id'], coup, position)
            print(dico)
        elif coup == 'MH':
            position = input("Préciser la position (x, y) et presser la touche ⏎: ")
            liste = dico['état']["murs"]["horizontaux"]
            liste.append(position)
            nbre_murs = dico['état']['joueurs'][0]['murs']
            nbre_murs += -1
            api.jouer_coup(dico['id'], coup, position)
        elif coup == 'MV':
            position = input("Préciser la position (x, y) et presser la touche ⏎: ")
            liste = dico['état']["murs"]["verticaux"]
            liste.append(position)
            nbre_murs = dico['état']['joueurs'][0]['murs']
            nbre_murs += -1
            api.jouer_coup(dico['id'], coup, position)
        else:
            raise ValueError("Ce type de coup n'existe pas")
        afficher_damier_ascii(dico)
        print(i)
        continue

jouer_jeu()
