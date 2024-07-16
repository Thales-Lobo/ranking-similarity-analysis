import json
from typing import Optional

def load_json_data(file_path: str, 
                    key: Optional[str] = None) -> json :
    """
    Loads JSON data from a file.

    Args:
    - file_path (str): Path to the JSON file.
    - key (str, optional): Optional key to retrieve specific data from JSON.

    Returns:
    - If key is provided, returns the value associated with the key.
    - Otherwise, returns the entire JSON data.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    if key:
        return data[key]
    else:
        return data