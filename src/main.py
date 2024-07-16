from utils.calculate.calculate_scores import calculate_scores
from utils.plot.plot_scores import plot_scores
from utils.plot.plot_average_scores_by_field import plot_average_scores_by_field
from utils.load_json_data import load_json_data

def main():
    """
    Main function to run the ranking similarity analysis.

    Loads reference vector and responses from JSON files, calculates similarity scores,
    and plots results.

    Args:
    - None

    Returns:
    - None

    Notes:
    - Assumes JSON files ('reference_vector.json' and 'responses.json') are located in 'src/data/' directory.
    - Uses functions from 'utils.calculate' and 'utils.plot' modules to perform calculations and plotting.
    """
    # Define paths to JSON files
    reference_file = 'src/data/dictionaries/reference_vector.json'
    responses_file = 'src/data/dictionaries/responses.json'

    # Load reference vector from JSON
    reference_vector = load_json_data(reference_file, 'reference_vector')

    # Load responses from JSON
    responses = load_json_data(responses_file, 'responses')

    # Calculate scores
    scores = calculate_scores(reference_vector, responses, weight_mode='variable')

    # Plot scores and responses
    plot_scores(scores)

    # Plot average scores by field
    plot_average_scores_by_field(scores)

if __name__ == "__main__":
    main()
