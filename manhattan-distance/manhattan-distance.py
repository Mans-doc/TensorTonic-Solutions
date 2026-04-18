import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    
    d = np.sum(np.abs(x-y))

    return float(d)

x = np.array([1,2,3])
y = np.array([2,4,6])

print(manhattan_distance(x, y))