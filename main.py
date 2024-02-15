from node import *
from graph import *
from ParcoursGraphes import *



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

Graph = Graph()
for value in dico :
    Graph.add_a_node(Node(value))
print(Graph)

print(cherche_chemin(Graph.adjacency_list,"lire","paie"))

print(dijkstra(Graph.adjacency_list,"lire","paie")) # on vois bien que djikstra est bien plus rapide sa mère la p***