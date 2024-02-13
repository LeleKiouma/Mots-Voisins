# -*- coding: utf-8 -*-

import graphviz as gv

def consecutif(word_1: str, word_2: str) -> bool:
    """
        check if two word have only one letter apart from each other
        Parameters:
        -----
            word_1: (str) the first word
            word_2: (str) the second word
        Return:
        -----
        (bool): True if thee is only one different letter from the first word to the second
    """
    word_1 = sorted(word_1)
    word_2 = sorted(word_2)
    for first_turn in range(len(word_1)):
        for second_turn in range(len(word_2)):
            if word_2[second_turn] == word_1[first_turn]:
                word_2.pop(second_turn)
                break
    if len(word_2) == 1:
        return True
    return False


def solve(beginning: str, to: str, list_of_words: list) -> list:
    """
    find a sequence of words that will take you from one word to the next
    Parameters:
        beginning (str): the first word
        to (str): the final word
        list_of_words (list): the list of word

    Returns:
        list: the path
    """
    graph = gv.Graph()
    added = []
    for element in list_of_words:
        graph.node(element, element)
        added.append(element)
        for element_2 in added:
            if consecutif(element,element_2) and element_2 != element:
                graph.edge(element_2, element)
    


dico = ["aime", "auge", "baie", "brie", "bris", "bure", "cage", "cale", "came", "cape",
"cime", "cire", "cris", "cure", "dame", "dime", "dire", "ducs", "dues", "duos",
"dure", "durs", "fart", "fors", "gage", "gaie", "gais", "gale", "gare", "gars",
"gris", "haie", "hale", "hors", "hure", "iris", "juge", "jure", "kart", "laie",
"lame", "lime", "lire", "loge", "luge", "mage", "maie", "male", "mare", "mari",
"mars", "mere", "mers", "mime", "mire", "mors", "muet", "mure", "murs", "nage",
"orge", "ours", "page", "paie", "pale", "pame", "pane", "pape", "pare", "pari",
"part", "paru", "pere", "pers", "pipe", "pire", "pore", "prie", "pris", "pues",
"purs", "rage", "raie", "rale", "rame", "rape", "rare", "rime", "rire", "sage",
"saie", "sale", "sape", "sari", "scie", "sure", "taie", "tale", "tape", "tare",
"tari", "tige", "toge", "tore", "tors", "tort", "trie", "tris", "troc", "truc"]

print(solve("ours", "cage", dico))
