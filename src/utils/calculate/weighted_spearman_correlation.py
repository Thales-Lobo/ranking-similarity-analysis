from typing import List
import numpy as np
from scipy.stats import rankdata

def weighted_spearman_correlation(list1: List[int],
                                    list2: List[int],
                                    weights: List[float],
                                    scale_factor: float = 3) -> float:
    """
    Calculate the weighted Spearman rank-order correlation coefficient between two lists.

    Args:
    - list1 (list): First ranking vector.
    - list2 (list): Second ranking vector.
    - weights (numpy.ndarray): Array of weights for each position in the vectors.
    - scale_factor (float): Factor to scale the numerator of the correlation calculation. 
                            Default is 3.

    Returns:
    - correlation (float): Weighted Spearman rank-order correlation coefficient.
    """
    # Ensure weights are numpy array
    weights = np.array(weights)
    
    # Normalize weights
    weights = weights / np.sum(weights)
    
    # Rank the lists
    rank1 = rankdata(list1)
    rank2 = rankdata(list2)

    # Calculate the differences
    d = rank1 - rank2
    n = len(list1)

    # Calculate the weighted sum of squared differences
    weighted_sum_d_squared = np.sum(weights * d ** 2)
    
    # Calculate the correlation coefficient
    numerator = 6 * weighted_sum_d_squared * scale_factor
    denominator = n * (n ** 2 - 1)
    
    correlation = 1 - (numerator / denominator)
    return correlation
