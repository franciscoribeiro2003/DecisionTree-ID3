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



    def classify(self, data):
        if self.root is None:
            raise Exception('Tree not trained')
        return self.root.classify(data)
    
    def print(self):
        if self.root is None:
            raise Exception('Tree not trained')
        self.root.print()

    def train(self):
        self.root = self.ID3(self.data, self.atributos, self.classe)
        return self.root
    
    def ID3(self, data, atributos, classe, depth=0):
        if len(data) == 0:
            return Node(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        if self.sameClass(data, classe):
            return Node(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, data[0][-1])
        if len(atributos) == 0 or depth == self.DEPTH:
            return Node(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.mostCommon(data, classe))
        else:
            best = self.chooseAtributo(data, atributos, classe)
            atributos.remove(best)
            root = Node(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, best)
            for v in self.getValues(data, best):
                newData = self.getSubData(data, best, v)
                subTree = self.ID3(newData, deepcopy(atributos), classe, depth+1)
                root.add(v, subTree)
            return root
        
    def sameClass(self, data, classe):
        for i in range(len(data)):
            if data[i][-1] != data[0][-1]:
                return False
        return True
    

    def mostCommon(self, data, classe):
        count = {}
        for i in data:
            if i[-1] in count:
                count[i[-1]] += 1
            else:
                count[i[-1]] = 1
        return max(count, key=count.get)

    def chooseAtributo(self, data, atributos, classe):
        best = None
        bestGain = 0
        for a in atributos:
            gain = self.gain(data, a, classe)
            if gain > bestGain:
                best = a
                bestGain = gain
        return best
    
    def gain(self, data, atributo, classe):
        gain = self.entropy(data, classe)
        for v in self.getValues(data, atributo):
            subData = self.getSubData(data, atributo, v)
            gain -= (len(subData)/len(data)) * self.entropy(subData, classe)
        return gain
    
    def entropy(self, data, classe):
        count = {}
        for i in data:
            if i[-1] in count:
                count[i[-1]] += 1
            else:
                count[i[-1]] = 1
        entropy = 0
        for i in count:
            entropy += (-count[i]/len(data)) * log2(count[i]/len(data))
        return entropy
    
    def getValues(self, data, atributo):
        values = []
        for i in data:
            if i[atributo] not in values:
                values.append(i[atributo])
        return values
    
    def getSubData(self, data, atributo, value):
        subData = []
        for i in data:
            if i[atributo] == value:
                subData.append(i)
        return subData
    