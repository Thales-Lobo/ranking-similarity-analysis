from typing import Optional, List, Dict
from utils.calculate.calculate_weights import calculate_weights
from utils.calculate.weighted_spearman_correlation import weighted_spearman_correlation
from utils.preference_to_positions import preference_to_positions

def calculate_scores(reference_vector: List[int],
                      responses: List[Dict],
                      weight_mode: Optional[str] = 'constant') -> Dict:
    """
    Calculate scores based on weighted Spearman's rank correlation coefficient between a reference vector
    and answer vectors from multiple responses.

    Args:
    - reference_vector (list): Reference vector representing the correct ranking.
    - responses (list): List of dictionaries, each containing 'name', 'answer_vector', and 'field'.
    - weight_mode (str, optional): Mode for weight calculation ('constant' or 'variable'). Default is 'constant'.

    Returns:
    - scores (list): List of dictionaries containing 'name', 'score', 'answer_vector', and 'field'.
      'score' represents the calculated similarity score as a percentage.

    Notes:
    - Uses weighted Spearman's rank correlation coefficient to measure similarity between reference and response vectors.
    - Scores are calculated as correlation * 100, where correlation is the weighted Spearman's rank correlation coefficient.
    """
    reference_vector = preference_to_positions(reference_vector)
    n = len(reference_vector)
    weights = calculate_weights(n, mode=weight_mode)
    scores = []

    for response in responses:
        name = response['name']
        answer_vector = preference_to_positions(response['answer_vector'])
        field = response['field']
        
        correlation = weighted_spearman_correlation(reference_vector, answer_vector, weights)
        print(f"{name} | {correlation}")
        # Convert to percentage
        score = correlation * 100
        print(f'"name": {name}, "score": {score}, "answer_vector": {answer_vector}, "field": {field}')
        scores.append({"name": name, "score": score, "answer_vector": answer_vector, "field": field})
    
    return scores
