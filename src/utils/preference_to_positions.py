from typing import List

def preference_to_positions(preferences: List[int]) -> List[int]:
    """
    Converts a preference list into a position list.
    
    Args:
        preferences (List[int]): A list of integers where each integer represents an item,
                                 and its position in the list represents its preference ranking.
                                 For example, [2, 3, 4, 1] means item 2 is the best, item 3 is second best, etc.
    
    Returns:
        List[int]: A list of integers where each integer represents the position of the corresponding item in the
                   original preference list. For example, input [2, 3, 4, 1] returns [4, 1, 2, 3].
    """
    n = len(preferences)
    positions = [0] * n

    for index, preference in enumerate(preferences):
        # The position of 'preference' in the original list is 'index + 1'
        positions[preference - 1] = index + 1

    return positions