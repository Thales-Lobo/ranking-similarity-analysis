def weighted_kendall_tau(reference, comparison, weights):
    """
    Calculate weighted Kendall's tau distance between two rankings.

    Args:
    - reference (list): Reference ranking vector.
    - comparison (list): Comparison ranking vector.
    - weights (numpy.ndarray): Array of weights for each position in the vectors.

    Returns:
    - distance (float): Weighted Kendall's tau distance between the reference and comparison rankings.

    Notes:
    - Kendall's tau distance measures the number of discordant pairs between two rankings.
    - Weighted version adjusts the influence of each pair based on provided weights.
    """
    n = len(reference)
    distance = 0
    normalization = 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            d_ij = 1 if (reference[i] - reference[j]) * (comparison[i] - comparison[j]) < 0 else 0
            distance += weights[i] * weights[j] * d_ij
            normalization += weights[i] * weights[j]
    
    return distance / normalization if normalization != 0 else 0