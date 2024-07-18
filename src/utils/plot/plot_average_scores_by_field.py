from collections import defaultdict
from typing import Dict, List
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_average_scores_by_field(scores: List[Dict],
                                dpi: int = 500) -> None:
    """
    Plot a bar chart showing average scores by field based on the given scores data.

    Args:
    - scores (list): List of dictionaries containing 'name', 'score', 'answer_vector', and 'field'.
    - dpi (int, optional): Dots per inch (DPI) for the saved image. Default is 500.

    Returns:
    - None

    Notes:
    - Calculates average scores for each field and plots them as a bar chart.
    - Each bar represents a field, with the height proportional to the average score.
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
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(fields, avg_scores, color='lightcoral', edgecolor='black')
    
    # Add annotations to bars
    for bar, count, avg in zip(bars, response_counts, avg_scores):
        height = bar.get_height()
        ax.annotate(f'{avg:.1f}%\n({count})',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    ax.set_xlabel('Field')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Scores by Field')
    
    # Save the plot as an image
    save_path = os.path.join('src', 'data', 'images', 'average_scores_by_field.png')
    plt.savefig(save_path, dpi=dpi)
    
    plt.show()
