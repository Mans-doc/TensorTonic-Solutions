import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    val, counts = np.unique(y, return_counts = True)

    prob = counts/np.sum(counts)
    entropy = -np.sum(prob*np.log2(prob))

    return entropy 

y = [1,1,1,1]

print(entropy_node(y))