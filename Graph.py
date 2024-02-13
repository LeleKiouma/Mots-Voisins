from Node import *
class graph:
    def __init__(self) -> None :
        """
        create the graph
        """
        self.list_of_node = []
        self.adjacency_list = {}
    def add_a_node(self,new_node:object) -> None: 
        """
        add a node to the graph
        Args:
            node (node_object): add the node and his neigbhour
        """
        for node in self.list_of_node:
            word_1 = sorted(node.value)
            word_2 = sorted(new_node.value)
            for first_turn in range(len(word_1)):
                for second_turn in range(len(word_2)):
                    if word_2[second_turn] == word_1[first_turn]:
                        word_2.pop(second_turn)
                        break
            if len(word_2) == 1:
                new_node.add_neighbor(node)
                node.add_neighbor(new_node)
        self.list_of_node.append(new_node)
        self.update_adjacency_list()
    def update_adjacency_list(self) -> None :
        """
        update the adjacency dict
        """
        for node in self.list_of_node :
            name_of_neighbor = []
            for neighbor in node.get_neighbor():
                name_of_neighbor.append(neighbor.value)
            self.adjacency_list.update({node.value:name_of_neighbor});
    
    def __str__(self) -> None :
        """
        print in a correct way the graph
        """
        print("Ce graphe contient " + str(len(self.list_of_node)) +" élement.\net les voici :")
        for node in self.list_of_node:
            print(node)
        return " "
