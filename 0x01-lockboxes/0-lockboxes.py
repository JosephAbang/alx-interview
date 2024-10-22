#!/usr/bin/python3
"""
    Solution to the LockBoxes problem
"""

def canUnlockAll(boxes):
    """
    Checks whether all boxes can be unlocked.
    
    Args:
    boxes: A list of lists, where each sublist contains keys to other boxes.
    
    Returns:
    True if every box can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    keys = set()
    unlocked_boxes = []
    current_box = 0

    while current_box < num_boxes:
        box_to_check = current_box
        unlocked_boxes.append(current_box)
        keys.update(boxes[current_box])
        
        for key in keys:
            if key != 0 and key < num_boxes and key not in unlocked_boxes:
                current_box = key
                break
        
        if box_to_check != current_box:
            continue
        else:
            break

    # Check if all boxes have been opened
    for i in range(num_boxes):
        if i not in unlocked_boxes and i != 0:
            return False
    
    return True