class Node :
    def __init__(self,value:str) -> None:
        """
        create the node
        Args:
            value (str): the value of the node
            neighbor (list): his neighbor
        """
        self.value = value
        self.neighbor = []
    
    def get_neighbor(self)->list:
        """
        return the neighbor of the node
        Returns:
            list: the neighbor of the node
        """
        return self.neighbor
    
    def __str__(self) -> None:
        """
        print the node in a good way
        """
        print("\tLa valeur du noeu est "+ self.value+", ces voisin sont :",end = "\n\t\t")
        for neighbor in self.neighbor:
            print(neighbor.value,end = ' , ')
        return " "
    
    def add_neighbor(self,neighbor:object) -> None :
        """
        add the neighbor to the node's neighbor's list
        Args:
            neighbor (object): _description_
        """
        self.neighbor.append(neighbor)
