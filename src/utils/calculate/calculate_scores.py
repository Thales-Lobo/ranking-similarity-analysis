from utils.calculate.calculate_weights import calculate_weights
from utils.calculate.weighted_kendall_tau import weighted_kendall_tau

def calculate_scores(reference_vector, responses):
    """
    Calculate scores based on weighted Kendall's tau distance between a reference vector
    and answer vectors from multiple responses.

    Args:
    - reference_vector (list): Reference vector representing the correct ranking.
    - responses (list): List of dictionaries, each containing 'name', 'answer_vector', and 'field'.

    Returns:
    - scores (list): List of dictionaries containing 'name', 'score', 'answer_vector', and 'field'.
      'score' represents the calculated similarity score as a percentage.

    Notes:
    - Uses weighted Kendall's tau distance to measure similarity between reference and response vectors.
    - Scores are calculated as (1 - distance) * 100, where distance is normalized weighted Kendall's tau distance.
    """
    n = len(reference_vector)
    weights = calculate_weights(n)
    scores = []

    for response in responses:
        name = response['name']
        answer_vector = response['answer_vector']
        field = response['field']
        
        distance = weighted_kendall_tau(reference_vector, answer_vector, weights)
        # Convert to percentage
        score = (1 - distance) * 100
        scores.append({"name": name, "score": score, "answer_vector": answer_vector, "field": field})
    
    return scores