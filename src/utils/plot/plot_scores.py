import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

def plot_scores(scores, dpi=500):
    """
    Plot a horizontal bar chart showing scores with fields in parentheses below names, sorted by scores in descending order.

    Args:
    - reference_vector (list): Reference vector representing the correct ranking.
    - scores (list): List of dictionaries containing 'name', 'score', 'answer_vector', and 'field'.
    - dpi (int): Dots per inch for saving the plot image (default is 500).

    Returns:
    - None

    Notes:
    - Plots a single horizontal bar chart sorted by scores in descending order.
    - Displays percentage score at the end of each bar.
    - Saves the plot as an image file in 'src/data/images/scores_chart.png'.
    """
    # Sort scores by descending score
    scores_sorted = sorted(scores, key=lambda x: x['score'], reverse=True)
    
    names = [score_data['name'] for score_data in scores_sorted]
    scores = [score_data['score'] for score_data in scores_sorted]
    fields = [score_data['field'] for score_data in scores_sorted]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    y_pos = np.arange(len(scores))
    bars = ax.barh(y_pos, scores, align='center', color='#6BAED6')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"{names[i]}\n({fields[i]})" for i in range(len(scores))], fontsize=12)
    ax.invert_yaxis()
    ax.set_xlabel('Scores (%)', fontsize=14)
    ax.set_title('Scores by Name and Field', fontsize=16)

    # Highlight the name of each person in bold
    for tick_label in ax.get_yticklabels():
        if tick_label.get_text().split()[0] in names:
            tick_label.set_fontweight('bold')
    
    # Add percentage score at the end of each bar
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{score:.2f}%', va='center', ha='left', fontsize=12)
    
    # Save the plot as an image with specified DPI
    save_path = os.path.join('src', 'data', 'images', 'scores_chart.png')
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
    
    plt.show()
