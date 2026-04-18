import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.asarray(x)

    f = np.where(x>=0, x , alpha*x)

    return f


x = [-2,-1,0,1,2]

print(leaky_relu(x, alpha=0.01))

    