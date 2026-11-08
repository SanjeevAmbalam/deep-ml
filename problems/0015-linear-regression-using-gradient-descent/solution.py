import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    # will compute gradients manually rather than via closed from
    e = 1e-6
    theta_grad = np.zeros((n,1))

    for i in range(iterations):
        theta_loss = 1/(2*m) * np.sum((X@theta-y)**2)     
        for k in range(n):
            theta_nudged = theta.copy()
            theta_nudged[k] += e
            theta_nudged_loss = 1/(2*m) * np.sum((X@theta_nudged-y)**2)
            theta_grad[k] = (theta_nudged_loss-theta_loss)/e

        theta-=alpha*theta_grad

    return theta.flatten()


