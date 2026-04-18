import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    
    d = np.sqrt(np.sum((x-y)**2))

    return float(d) 

x=np.array([3,4])
y=np.array([0,0])

print(euclidean_distance(x, y))