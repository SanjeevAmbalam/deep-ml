import math

def tanh(x: float) -> float:
    """
    Implements the Tanh (hyperbolic tangent) activation function.

    Args:
        x (float): Input value

    Returns:
        float: The tanh of the input, rounded to 4 decimal places
    """
    # Your code here
    out = (math.exp(2*x)-1)/(math.exp(2*x)+1)
    return round(out, 4)