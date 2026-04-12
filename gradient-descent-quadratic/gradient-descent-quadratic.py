def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for i in range(steps):
        gradient = 2*a*x0 + b
        x0 = x0 - lr*gradient

    return x0

a=1
b=-4
c=3
x0=0
lr=0.1
steps=50

print(gradient_descent_quadratic(a, b, c, x0, lr, steps))
        

    