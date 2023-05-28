import math
from collections import Counter

def calculate_entropy(data):
    label_counts = Counter(data)
    entropy = 0.0
    total_examples = len(data)

    for label in label_counts:
        probability = label_counts[label] / total_examples
        entropy -= probability * math.log2(probability)

    return entropy

def is_numerical(attribute_values):
    try:
        float(attribute_values[0])
        return True
    except ValueError:
        return False

def select_best_attribute(examples, attributes, target_attribute):
    target_index = attributes[target_attribute]
    base_entropy = calculate_entropy([example[target_index] for example in examples])
    best_info_gain = 0.0
    best_attribute = None

    for attribute, index in attributes.items():
        if attribute != target_attribute:
            attribute_values = [example[index] for example in examples]
            if is_numerical(attribute_values):
                attribute_values = [float(value) for value in attribute_values]  # Convert to float
                attribute_values = sorted(attribute_values)
                thresholds = [(attribute_values[i] + attribute_values[i+1]) / 2 for i in range(len(attribute_values)-1)]
                for threshold in thresholds:
                    subset_less = [example for example in examples if float(example[index]) <= threshold]
                    subset_greater = [example for example in examples if float(example[index]) > threshold]
                    subset_labels_less = [example[target_index] for example in subset_less]
                    subset_labels_greater = [example[target_index] for example in subset_greater]
                    probability_less = len(subset_less) / len(examples)
                    probability_greater = len(subset_greater) / len(examples)
                    new_entropy = (probability_less * calculate_entropy(subset_labels_less)
                                   + probability_greater * calculate_entropy(subset_labels_greater))
                    info_gain = base_entropy - new_entropy

                    if info_gain > best_info_gain:
                        best_info_gain = info_gain
                        best_attribute = (attribute, threshold)
            else:
                attribute_values = set(attribute_values)
                new_entropy = 0.0

                for value in attribute_values:
                    subset = [example for example in examples if example[index] == value]
                    subset_labels = [example[target_index] for example in subset]
                    probability = len(subset) / len(examples)
                    new_entropy += probability * calculate_entropy(subset_labels)

                info_gain = base_entropy - new_entropy

                if info_gain > best_info_gain:
                    best_info_gain = info_gain
                    best_attribute = attribute

    return best_attribute

def ID3(examples, attributes, target_attribute):
    target_index = attributes[target_attribute]
    class_labels = [example[target_index] for example in examples]

    # If all examples have the same class label, return the label
    if len(set(class_labels)) == 1:
        return class_labels[0]

    # If there are no more attributes to split on, return the majority class label
    if len(attributes) == 1:
        majority_label = Counter(class_labels).most_common(1)[0][0]
        return majority_label

    # Select the best attribute to split on
    best_attribute = select_best_attribute(examples, attributes, target_attribute)

    # Create a new decision tree with the best attribute as the root
    tree = {best_attribute: {}}

    if isinstance(best_attribute, tuple):  # Numerical attribute
        attribute, threshold = best_attribute
        tree[best_attribute]['<= ' + str(threshold)] = ID3([example for example in examples if float(example[attributes[attribute]]) <= threshold],
                                                           attributes, target_attribute)
        tree[best_attribute]['> ' + str(threshold)] = ID3([example for example in examples if float(example[attributes[attribute]]) > threshold],
                                                          attributes, target_attribute)
    else:  # Categorical attribute
        remaining_attributes = attributes.copy()
        remaining_attributes.pop(best_attribute)
        attribute_index = attributes[best_attribute]
        attribute_values = set([example[attribute_index] for example in examples])

        for value in attribute_values:
            subset = [example for example in examples if example[attribute_index] == value]
            subtree = ID3(subset, remaining_attributes, target_attribute)
            tree[best_attribute][value] = subtree

    return tree

def print_decision_tree(tree, indent=''):
    if isinstance(tree, dict):
        for attribute, subtree in tree.items():
            print(f"{indent}{attribute}:")
            print_decision_tree(subtree, indent + "\t")
    else:
        print(f"{indent}{tree}")