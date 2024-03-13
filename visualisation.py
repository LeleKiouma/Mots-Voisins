# -*- coding: utf-8 -*-

import graphviz as gv
import node
import graph

def add_a_node(word_1:str,word_2:str) -> bool: 
    """
    add a node to the graph by :
    Args:
        word_1 (str): the first word
        word_2 (str): the second
    """
    word_1 = sorted(word_1)  
    word_2 = sorted(word_2) 
    for first_turn in range(len(word_1)):
        for second_turn in range(len(word_2)):
            if word_2[second_turn] == word_1[first_turn]:
                word_2.pop(second_turn) 
                break
    if len(word_2) == 1 : #this mean the word_2 and the word_1 have only 1 caracter different
        return True     #add the two word in their own neighbor
    return False


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

Graph =  gv.Graph() 
list_of_check_word = []
for value in dico :
    for word in list_of_check_word :
        if add_a_node(word,value) :
            Graph.edge(value,word)
    list_of_check_word.append(value)

print(Graph.source)  

Graph.view()