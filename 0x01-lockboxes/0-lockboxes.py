def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    keys = set([0])  # Initialize with keys for the first box

    for box_index in range(len(boxes)):
        if box_index in keys:
            keys.update(boxes[box_index])  # Add keys in the current box to the set

    # Check if all boxes are reachable
    return all(box_index in keys for box_index in range(len(boxes)))
