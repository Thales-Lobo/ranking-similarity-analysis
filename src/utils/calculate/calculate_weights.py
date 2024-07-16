from typing import Optional, List
import numpy as np

def calculate_weights(n: int,
                    alpha: Optional[float] = 1.0,
                    mode: Optional[str] = 'constant') -> List[float]:
    """
    Calculate weights for weighted Spearman's rank correlation based on the number of elements and mode.

    Args:
    - n (int): Number of elements in the vectors.
    - alpha (float, optional): Scaling factor for weights. Default is 1.
    - mode (str, optional): Mode for weight calculation ('constant' or 'variable'). Default is 'constant'.

    Returns:
    - weights (numpy.ndarray): Array of weights corresponding to each position in the vectors.

    Notes:
    - 'constant' mode assigns equal weights to all positions.
    - 'variable' mode uses an exponential decay function adjusted to assign higher weights to the start and end,
      with the start being slightly more important than the end, and the middle being the least important.
    """
    if mode == 'constant':
        weights = np.ones(n)
    elif mode == 'variable':
        # Define the decay rate
        beta = 0.5 / (n - 1)
        
        # Calculate weights with adjusted exponential decay
        weights = np.array([alpha * (np.exp(-beta * abs(i - (n - 1) / 2)) + 0.1 * np.exp(-beta * i)) for i in range(n)])
    else:
        raise ValueError("Invalid mode. Choose 'constant' or 'variable'.")
    
    return weights