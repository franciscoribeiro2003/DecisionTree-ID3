import pandas as pd
import decisiontree as dt
from sys import argv

examples = pd.read_csv(argv[1])
attributes = [attr for attr in examples]
classX = attributes[-1]
attributes.pop(0)
attributes.pop(-1)

tree = dt.ID3(examples, attributes, classX)
dt.printTree(tree)
