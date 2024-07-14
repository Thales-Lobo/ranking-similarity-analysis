import numpy as np

def calculate_weights(n, alpha=1):
    """
    Calculate weights for weighted Kendall's tau distance based on the number of elements.

    Args:
    - n (int): Number of elements in the vectors.
    - alpha (float, optional): Scaling factor for weights. Default is 1.

    Returns:
    - weights (numpy.ndarray): Array of weights corresponding to each position in the vectors.

    Notes:
    - Uses an exponential decay function to assign weights, with higher weights for first, second, and last positions.
    - Intermediate positions have decreasing weights based on an exponential decay function.
    """
    beta = 1 / (n - 3)
    
    # Calculate intermediate weights
    intermediate_weights = [alpha * np.exp(-beta * (i - 3)) for i in range(3, n)]
    w_med = np.mean(intermediate_weights)
    
    # Define specific weights
    W1 = 2 * w_med
    W2 = 2 * w_med
    Wn = 1.5 * w_med
    
    # Combine all weights
    weights = np.zeros(n)
    weights[0] = W1
    weights[1] = W2
    weights[-1] = Wn
    
    for i in range(2, n-1):
        weights[i] = alpha * np.exp(-beta * (i - 2))
    
    return weights