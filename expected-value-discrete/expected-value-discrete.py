import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    is_valid = np.allclose(np.sum(p), 1)
    if not is_valid:
        raise ValueError("Probabilities sum must be 1")

    result = np.sum(np.multiply(x,p))
    return result

p=np.array([0.2, 0.5, 0.3])
x=np.array([1, 2, 3])

print(expected_value_discrete(x, p))
