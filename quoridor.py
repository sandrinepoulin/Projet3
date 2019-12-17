'''
Projet servant à suivre une partie et avoir une fonction
déterminant le meilleur coup possible
'''
import networkx as nx


class QuoridorError(Exception):
    '''Pour que l'erreur existe'''


### Pour le Graphe, pas touche!
def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """
    Crée le graphe des déplacements admissibles pour les joueurs.

    :param joueurs: une liste des positions (x,y) des joueurs.
    :param murs_horizontaux: une liste des positions (x,y) des murs horizontaux.
    :param murs_verticaux: une liste des positions (x,y) des murs verticaux.
    :returns: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):

        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe


class Quoridor:
    '''Classe permettant à de jouer à Quorridor'''

    def __init__(self, joueurs, murs=None):
        '''Méthode d'initiation'''

        if not isinstance(joueurs, tuple):
            raise QuoridorError("'joueurs' doit être un itérable")
        elif len(joueurs) > 2:
            raise QuoridorError("seulement 2 joueurs acceptés")
        elif isinstance(joueurs[0], str) and isinstance(joueurs[1], str):
            self.joueurs = [{'nom': joueurs[0], 'murs': 10, 'pos': (5, 1)},
                            {'nom': joueurs[1], 'murs': 10, 'pos': (5, 9)}]
            self.murs = {'horizontaux': [], 'verticaux': []}

        elif isinstance(joueurs[0], dict) and isinstance(joueurs[1], dict):

            if joueurs['joueurs'][0]['murs'] or joueurs['joueurs'][0]['murs'] < 0:
                raise QuoridorError('nombre de murs invalide')
            if joueurs['joueurs'][0]['murs'] or joueurs['joueurs'][0]['murs'] > 10:
                raise QuoridorError('nombre de murs invalide')

            elif joueurs['joueurs'][0]['pos'][0] or joueurs['joueurs'][0]['pos'][1] < 0:
                raise QuoridorError('postion(s) invalide(s)')

            elif joueurs['joueurs'][1]['pos'][0] or joueurs['joueurs'][1]['pos'][1] < 0:
                raise QuoridorError('postion(s) invalide(s)')

            elif joueurs['joueurs'][0]['pos'][0] or joueurs['joueurs'][0]['pos'][1] > 9:
                raise QuoridorError('postion(s) invalide(s)')

            elif joueurs['joueurs'][1]['pos'][0] or joueurs['joueurs'][1]['pos'][1] > 9:
                raise QuoridorError('postion(s) invalide(s)')

            elif not isinstance(murs, dict):
                raise QuoridorError("l'argument 'murs' n'est pas un dictionnaire")

            elif joueurs['joueurs'][0]['murs'] + joueurs['joueurs'][1]['murs'] + len(joueurs['murs']['horizontaux']) + len(joueurs['murs']['verticaux']) != 20:
                raise QuoridorError("le total des murs placés et plaçables n'est pas égal à 20")

            for i in murs['horizontaux']:
                if 1 > i[0] > 8 or 2 > i[1] > 9:
                    raise QuoridorError("la position d'un mur est invalide")

            for i in murs['verticaux']:
                if 2 > i[0] > 9 or 1 > i[1] > 8:
                    raise QuoridorError("la position d'un mur est invalide")
            self.joueurs = joueurs
            self.murs = murs
        self.état_partie()

    def __str__(self):
        '''Fonction qui donne le damier de jeu'''

        dico = self.état_partie()
        
        leg = 'Légende: 1: ' + self.joueurs[0]['nom'] + ' 2: ' + self.joueurs[1]['nom'] + '\n'

        top = ' '*3 + '-'*35 + ' \n'

        temp_middle = []
        empty_mid_section = ' '*2 + '|' + ' '.join(['   ']*9) + '|\n'

        for i in list(range(1, 10))[::-1]:
            temp_middle.append(f'{i} |' + ' '.join([' . ']*9) + '|\n')

        middle = empty_mid_section.join(temp_middle)

        bot = '--|' + '-'*35 + ' \n'
        bot += '  | ' + '   '.join([f'{i}' for i in range(1, 10)])
        board = ''.join([leg, top, middle, bot])

        #Mettre le damier en liste
        board_split = [list(ligne) for ligne in board.split('\n')]

            #PLACER JOUEUR
        #position  joueur 1
        x1, y1 = dico["joueurs"][0]['pos']
        board_split[-2*y1+20][x1*4] = '1'

        #position joueur 2
        x2, y2 = dico["joueurs"][1]['pos']
        board_split[-2*y2+20][x2*4] = '2'

            #PLACER MURS
        #placer murs horizontaux
        for placement in range(len(dico["murs"]["horizontaux"])):
            x, y = dico["murs"]["horizontaux"][placement]
            for variable in range(7):
                board_split[-2*y+21][4*x-1+variable] = '-'

        #placer murs verticaux
        for placement in range(len(dico["murs"]["verticaux"])):
            x, y = dico["murs"]["verticaux"][placement]
            for variable in range(3):
                board_split[-2*y+18+variable][4*x-2] = '|'

        #Remettre le damier en str
        rep = '\n'.join([''.join(elem) for elem in board_split])
        return rep


    def déplacer_jeton(self, joueur, position):
        '''Méthode qui détermine les déplacements possibles'''

        self.graphe = construire_graphe(
            [joueur['pos'] for joueur in self.état_partie()['joueurs']],
            self.état_partie()['murs']['horizontaux'],
            self.état_partie()['murs']['verticaux'])

        # On doit s'assurer que le nombre qui représente le joueur est valide
        # que la position existe et est accessible
        if joueur in {1, 2}:
            if 0 < position[0] < 10 and 0 < position[1] < 10:
                if position in list(self.graphe.successors(self.joueurs[joueur - 1]['pos'])):
                    self.joueurs[joueur - 1]['pos'] = position
                else:
                    raise QuoridorError("Cette case n'est pas accessible")
            else:
                raise QuoridorError("Cette case n'existe pas")
        else:
            raise QuoridorError('Le numéro du joueur doit être 1 ou 2')

    def état_partie(self):
        '''Cette fonction produit/retourne l'état actuel de la partie'''
        self.état = {'joueurs': self.joueurs, 'murs': self.murs}
        return self.état


    def jouer_coup(self, joueur):
        '''Fonction qui détermine le meileur coup possible'''
        self.graphe = construire_graphe(
            [joueur['pos'] for joueur in self.état_partie()['joueurs']],
            self.état['murs']['horizontaux'],
            self.état['murs']['verticaux'])
        # On trouve le chemin le plus court et se déplace dans cette direction
        if joueur in {1, 2}:
            path = nx.shortest_path(self.graphe, self.joueurs[joueur-1]['pos'], f'B{joueur}')
            if self.partie_terminée() is False:
                self.déplacer_jeton(joueur, path[1])
            else:
                raise QuoridorError('La partie est terminée')
        else:
            raise QuoridorError('Le numéro du joueur doit être 1 ou 2')

    def partie_terminée(self):
        '''Déterminer si la partie est terminée.'''

        if self.état['joueurs'][0]['pos'][1] == 9:
            return 'Le gagnant  est {}'.format(self.joueurs[0]['nom'])
        if self.état['joueurs'][1]['pos'][1] == 1:
            return 'Le gagnant  est {}'.format(self.joueurs[1]['nom'])
        return False

    def placer_mur(self, joueur, position, orientation):
        '''Placer les murs'''

        if joueur in {1, 2}:
            if self.joueurs[joueur - 1]['murs'] != 0:
                self.joueurs[joueur - 1]['murs'] -= 1
            else:
                raise QuoridorError("Ce joueur n'a plus de murs.")
        else:
            raise QuoridorError("Le numéro du joueur doit être 1 ou 2.")
        
        # murs horizontaux
        if orientation == 'horizontal':
            if 1 > position[0] > 8 or 2 > position[1] > 9:
                raise QuoridorError('Impossible de placer un mur à cet endroit')

            elif position in self.murs['horizontaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0] + 1, position[1]) in self.murs['horizontaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0] - 1, position[1]) in self.murs['horizontaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0] + 1, position[1] - 1) in self.murs['verticaux']:
                raise QuoridorError('Un mur déjà placé bloque cet endroit')

            self.murs['horizontaux'].append(position)

        # murs verticaux
        elif orientation == 'vertical':
            if 2 > position[0] > 9 or 1 > position[1] > 8:
                raise QuoridorError('Impossible de placer un mur à cet endroit')
            elif position in self.murs['verticaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0], position[1] - 1) in self.murs['verticaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0], position[1] + 1) in self.murs['verticaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            elif (position[0] - 1, position[1] + 1) in self.murs['horizontaux']:
                raise QuoridorError('Il y a déjà un mur à cet endroit')

            self.murs['verticaux'].append(position)


'''game = Quoridor(('gager41', 'sapou51'))
game.jouer_coup(1)
game.jouer_coup(2)
print(game)'''
