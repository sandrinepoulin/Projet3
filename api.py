'''Le module api traite les fonctions qui communiquent avec e servuer par le module request'''
import requests


def lister_parties(idul):
    '''Cette fonction liste les dernières parties d'un idul donné'''
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        return rep
    else:
        return f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}."

def débuter_partie(idul):
    '''Cette fonction permet de debuter une partie'''
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError(rep['message'])
        return rep
    else:
        return f"Le Post sur {url_base+'débuter'} a produit le code d'erreur {rep.status_code}."


def jouer_coup(id_partie, type_coup, pos):
    '''Cette fonction permet de jouer un coup'''
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': pos})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError(rep['message'])
        elif 'gagnant' in rep:
            raise StopIteration('nom du gagnant')   ### trouver comment entrer le nom du gagnant
        return rep

    else:
        return f"Le Post sur {url_base+'jouer'} a produit le code d'erreur {rep.status_code}."
