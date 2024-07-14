# Ranking Similarity Analysis

![Python](https://img.shields.io/badge/python-3.7%2B-blue)

Analyze and visualize the similarity of ranking lists using Weighted Kendall's Tau distance.

## Table of Contents
- 📚 [Introduction](#introduction)
- ✨ [Features](#features)
- 🛠 [Installation](#installation)️
- 🚀 [Usage](#usage)
- 📧 [Contact](#contact)

## Introduction
This project implements an algorithm to compare ranking lists using Weighted Kendall's Tau distance. It calculates weights, evaluates similarity scores, and visualizes the results through various plots. The algorithm considers the importance of specific positions in the ranking and provides a clear way to interpret the scores.

## Features
- Calculate Weighted Kendall's Tau distance.
- Define custom weights for ranking positions.
- Visualize individual scores and their rankings.
- Plot average scores by group field.
- Saves the generated images in the directory `src/data/images/`

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
    pip install -r requirements.txt
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

    ```python
    python src/main.py
    ```

## Contact
For any questions, feel free to reach out to me:
- GitHub: [Thales-Lobo](https://github.com/Thales-Lobo)
- Email: thalesloboZ@gmail.com
