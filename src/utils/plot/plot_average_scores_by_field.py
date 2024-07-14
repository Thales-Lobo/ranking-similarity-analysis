from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_average_scores_by_field(scores):
    """
    Plot a pie chart showing average scores by field based on the given scores data.

    Args:
    - scores (list): List of dictionaries containing 'name', 'score', 'answer_vector', and 'field'.

    Returns:
    - None

    Notes:
    - Calculates average scores for each field and plots them as a pie chart.
    - Each slice of the pie represents a field, with the size proportional to the average score.
    - Saves the plot as an image file in 'src/data/images/average_scores_by_field.png'.
    """
    field_scores = defaultdict(list)
    
    for score_data in scores:
        field = score_data['field']
        score = score_data['score']
        field_scores[field].append(score)
    
    fields = list(field_scores.keys())
    avg_scores = [np.mean(field_scores[field]) for field in fields]
    response_counts = [len(field_scores[field]) for field in fields]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(avg_scores, labels=[f"{fields[i]} ({response_counts[i]})" for i in range(len(fields))], autopct='%1.1f%%', startangle=140)
    ax.set_title("Average Scores by Field")
    
    # Save the plot as an image
    save_path = os.path.join('src', 'data', 'images', 'average_scores_by_field.png')
    plt.savefig(save_path)
    
    plt.show()
