import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    N,D = X.shape
    w=np.zeros(D)
    b=0.0
    
    for i in range (steps):
        P = _sigmoid(X.dot(w)+b)
        
        error = P - y
        dw = X.T.dot(error)
        db = np.mean(error)
    
        w -= lr*dw
        b -= lr*db
    
    return (w, b)


X = np.array([[0],[1],[2],[3]])
y = np.array([0,0,1,1])
lr = 0.1
steps = 500
    
    
    