# Ranking Similarity Analysis

![Python](https://img.shields.io/badge/python-3.7%2B-blue)

Analyze and visualize the similarity of ranking lists using Weighted Spearman's Rank Correlation.

## Table of Contents
- 📚 [Introduction](#introduction)
- ♾️ [Mathematical Formulation](#mathematical-formulation)
- ✨ [Features](#features)
- 🛠 [Installation](#installation)
- 🚀 [Usage](#usage)
- 📧 [Contact](#contact)

## Introduction
This project implements an algorithm to compare ranking lists using Weighted Spearman's Rank Correlation. It calculates weights, evaluates similarity scores, and visualizes the results through various plots. The algorithm considers the importance of specific positions in the ranking and provides a clear way to interpret the scores.
### Mathematical Formulation

The Weighted Spearman's Rank Correlation is defined as:

![Equation](https://miro.medium.com/v2/resize:fit:688/format:webp/1*CCl_9w_HKMZp8lFmrMz9FQ.png)

- **Weights:** The correlation calculation incorporates weights (`w_i`) assigned to each position in the vectors. These weights reflect the importance of different ranks in the correlation calculation.
  
- **Scale Factor:** A `linear_scale_factor` is applied to adjust the numerator of the correlation calculation. This factor influences the final correlation value, allowing for customization based on specific needs. The default value is set to 2.5. In the same way, an `exponencial_scale_factor` is also applied to further adjust the numerator of the correlation calculation. The default value is set to 2.0.

- **Weight Distribution:** The weights are designed to emphasize positions at the beginning and end of the vectors more than those in the middle. This distribution ensures that ranks at these critical positions contribute more significantly to the correlation score.

## Features
- Calculate Weighted Spearman's Rank Correlation.
- Define custom weights for ranking positions with smooth decay for intermediate terms.
- Visualize individual scores and their rankings.
- Plot average scores by group field.
- Saves the generated images in the directory `src/data/images/`.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ranking-similarity-analysis.git
    cd ranking-similarity-analysis
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    ./run.sh --install|-i
    ```

## Usage
1. **Define your reference ranking and responses in JSON files (`reference_vector.json` and `responses.json`):**
    - `reference_vector.json` should contain the reference ranking vector.
    - `responses.json` should contain the responses from different individuals.

2. **Example structure of `src/data/dictionaries/reference_vector.json`:**
    ```json
    {
      "reference_vector": [3, 4, 1, 2]
    }
    ```

3. **Example structure of `src/data/dictionaries/responses.json`:**
    ```json
    {
      "responses": [
        {"name": "Alice", "answer_vector": [3, 2, 4, 1], "field": "Friends"},
        {"name": "Bob", "answer_vector": [2, 4, 1, 3], "field": "Family"},
        {"name": "Charlie", "answer_vector": [3, 4, 1, 2], "field": "Friends"},
        {"name": "David", "answer_vector": [1, 2, 3, 4], "field": "Colleagues"}
      ]
    }
    ```

4. Run the analysis from `src/main.py`:
    ```bash
    ./run.sh
    ```

5. You can clean the images folder if you want:
    ```bash
    ./run.sh --clean|-c
    ```

## Project Structure
The project is structured as follows:

```bash
.
├── README.md
├── config
│   └── requirements.txt
├── run.sh
└── src
    ├── data
    │   ├── dictionaries
    │   │   ├── reference_vector.json
    │   │   └── responses.json
    │   └── images
    │       ├── average_scores_by_field.png
    │       └── scores_chart.png
    ├── main.py
    └── utils
        ├── calculate
        │   ├── calculate_scores.py
        │   ├── calculate_weights.py
        │   └── weighted_spearman_correlation.py
        └── plot
            ├── plot_average_scores_by_field.py
            └── plot_scores.py
```

- **`README.md`**: Documentação principal do projeto.
- **`config/requirements.txt`**: Arquivo de requisitos para instalação de pacotes.
- **`run.sh`**: Script para automação de tarefas.
- **`src/`**: Diretório principal do código-fonte.
  - **`data/`**: Dados utilizados pelo projeto.
  - **`main.py`**: Ponto de entrada principal para execução do projeto.
  - **`utils/`**: Módulos utilitários.

## Contact
For any questions, feel free to reach out:
- GitHub: [Thales-Lobo](https://github.com/Thales-Lobo)
- Email: thalesloboZ@gmail.com
