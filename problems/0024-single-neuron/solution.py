import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    labels = np.array(labels)
    weights = np.array(weights)
    features = np.array(features)

    z = features@weights+bias
    probabilities = 1/(1+np.exp(-z))
    mse = np.mean((probabilities-labels)**2)
    return np.round(probabilities, 4).tolist(), round(float(mse),4)