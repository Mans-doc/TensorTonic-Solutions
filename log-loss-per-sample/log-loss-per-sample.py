import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    loss = []
    for y,p in zip (y_true, y_pred):
        
        p_hat = max(eps, min(p, 1-eps))
    
        L = -(y*math.log(p_hat)+(1-y)*math.log(1-p_hat))
    
        loss.append(L)

    return loss

y_true = [1,0,1]
y_pred = [0.9, 0.1, 0.8]
    