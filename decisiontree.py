import numpy as np
from collections import Counter

class Node:
    def __init__(self):
        self.children = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""

def ID3(examples, target_attribute, attributes):
    root = Node()

    # Check if all examples are positive
    if all(row[target_attribute] == '+' for row in examples):
        root.label = '+'
        return root

    # Check if all examples are negative
    if all(row[target_attribute] == '-' for row in examples):
        root.label = '-'
        return root

    # Check if no predicting attributes are left
    if not attributes:
        root.label = get_most_common_label(examples, target_attribute)
        return root

    best_attr = get_best_attribute(examples, target_attribute, attributes)
    root.attribute = best_attr

    for value in get_unique_values(examples, best_attr):
        subset_examples = [row for row in examples if row[best_attr] == value]

        if not subset_examples:
            leaf = Node(label=get_most_common_label(examples, target_attribute))
            root.add_child(value, leaf)
        else:
            new_attributes = attributes.copy()
            new_attributes.remove(best_attr)
            subtree = ID3(subset_examples, target_attribute, new_attributes)
            root.add_child(value, subtree)

    return root

def get_most_common_label(examples, target_attribute):
    labels = [row[target_attribute] for row in examples]
    label_counts = Counter(labels)
    most_common_label = label_counts.most_common(1)[0][0]
    return most_common_label

def get_best_attribute(examples, target_attribute, attributes):
    # Implement the logic to select the best attribute based on a suitable criterion
    # For example, you can use information gain or Gini index
    # Here, we'll assume a simple random selection
    return attributes[0]

def get_unique_values(examples, attribute):
    values = set()
    for row in examples:
        values.add(row[attribute])
    return values