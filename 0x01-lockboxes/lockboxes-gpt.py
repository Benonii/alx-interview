def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # Set to store the indices of opened boxes
    queue = [0]  # Queue for BFS traversal

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        for key in keys:
            if key < n and key not in opened:  # Check if the key is valid and not already opened
                opened.add(key)
                queue.append(key)

    return len(opened) == n
