#!/usr/bin/python3

''' Can I open all the boxes '''

from queue import Queue


def canUnlockAll(boxes):
    ''' Returns a boolean determining if you can open all boxes or not '''
    keys = set()
    opened_boxes = [boxes[0] if boxes and boxes[0] != [] else None]

    def get_keys(boxes):
        """ Gets all the keys for the boxes recursively """
        for item in boxes:
            if isinstance(item, list):
                get_keys(item)
            else:
                keys.add(item)

        return keys

    if boxes:
        for key in boxes[0]:
            if key < len(boxes): opened_boxes.append(boxes[key])

    closed_boxes = [box for box in boxes if box not in opened_boxes]

    for box in boxes:
        if box in opened_boxes:
            continue
        else:
            keys = get_keys(opened_boxes)
            if boxes.index(box) in keys:
                opened_boxes.append(box)
                closed_boxes.remove(box)
            else:
                return False
    return True
