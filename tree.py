from copy import deepcopy
import shutil


class DecisionTree:
    
    # Define max depth of the tree
    DEPTH = 4

    def __init__(self, data, atributos, classe):
        self.root = None
        self.data = data
        self.atributos = atributos
        self.classe = classe



  
