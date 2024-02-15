#author : Hugues Malherbe

import math

def cherche_chemin(graphe, depart,arrivee):
    """
    recherche d'un chemin dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: un chemin entre le sommet départ et le sommet arrivee s'il en existe au moins un ou None sinon
    """
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                return chemin + [arrivee]
            pile.append((voisin,chemin + [voisin]))
    return None


def cherche_tous_chemins(graphe, depart,arrivee):
    """
    recherche tous les chemins dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: tous les chemins entre le sommet départ et le sommet arrivee
    """
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return chemins
    pile = [(depart,[depart])]
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                chemins.append(chemin + [arrivee])
            pile.append((voisin,chemin + [voisin]))
    return chemins

def cherche_chemin_plus_court(graphe, depart,arrivee):
    """
    recherche le chemin le plus court chemin dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    chemins = cherche_tous_chemins(graphe,depart,arrivee)
    if len(chemins) == 0:
        return None
    lg_chemin_min = len(chemins[0])
    chemin_min = chemins[0]
    for chemin in chemins:
        if len(chemin) < lg_chemin_min:
            lg_chemin_min = len(chemin)
            chemin_min = chemin.copy()
    return chemin_min

def cherche_cycles(graphe, sommet):
    """
    recherche tous les cycles de sommet sommet dans le graphe graphe
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet du cycle
    :return: la liste des cycles de sommet sommet du graphe graphe
    """
    cycles = []
    for autre_sommet in graphe.keys():
        if autre_sommet in graphe[sommet]:
            chemins = cherche_tous_chemins(graphe, sommet, autre_sommet)
            for chemin in chemins:
                cycles.append(chemin + [sommet])
            cycles.extend(chemins)
    return cycles

def parcours_en_largeur(graphe, sommet):
    """
    Parcours d'un graphe en largeur
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet de départ du graphe étudié
    :return: la liste des sommets du graphe
    >>> parcours_en_largeur({"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")},"A")
    ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']
    """
    if not(sommet in graphe.keys()):
        return None
    F = [sommet]
    liste_sommets = []
    while len(F) != 0:
        S = F[0]
        for voisin in graphe[S]:
            if not(voisin in liste_sommets) and not(voisin in F):
                F.append(voisin)
        liste_sommets.append(F.pop(0))
    return liste_sommets


def parcours_en_profondeur(graphe, sommet):
    """
    Parcours d'un graphe en profondeur
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet de départ du graphe étudié
    :return: la liste des sommets du graphe
    >>> parcours_en_profondeur({"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")},"A")
    ['A', 'E', 'G', 'H', 'F', 'D', 'C', 'B']
    """
    if not(sommet in graphe.keys()):
        return None
    P = [sommet]
    liste_sommets = []
    while len(P) != 0:
        S = P.pop()
        liste_sommets.append(S)
        for voisin in graphe[S]:
            if not(voisin in liste_sommets) and not(voisin in P):
                P.append(voisin)
    return liste_sommets

def cherche_tous_cycles(graphe):
    """
    recherche tous les cycles dans le graphe graphe
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :return: la liste des cycles du graphe graphe
    """
    tous_cycles = []
    for sommet in graphe.keys():
        cycles = cherche_cycles(graphe, sommet)
        if cycles != []:
            tous_cycles.append(cycles)
    return tous_cycles


def trouve_min(noeuds,distances):
    mini = math.inf
    sommet = -1
    for s in noeuds:
        if distances[s] < mini:
            mini = distances[s]
            sommet = s
    return sommet

def maj_distances(s1,s2,distances,predecesseur):
    if distances[s2] > distances[s1] + 1:
        distances[s2] = distances[s1] + 1
        predecesseur[s2] = s1


def dijkstra(graphe,depart,arrivee):
    distances = {}
    predecesseur = {}
    for s in graphe.keys():
        distances[s] = math.inf
    distances[depart] = 0
    noeuds = list(graphe.keys())
    while len(noeuds) > 0:
        s1 = trouve_min(noeuds,distances)
        if s1 == -1:
            return None
        noeuds.remove(s1)
        for s2 in graphe[s1]:
            maj_distances(s1,s2,distances,predecesseur)
    A = []
    s = arrivee
    while s != depart:
        A.insert(0,s)
        if s in predecesseur.keys():
            s = predecesseur[s]
        else:
            return None
    A.insert(0,depart)
    return A