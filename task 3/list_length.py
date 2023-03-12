def estimate_length(collection : list):
    if len(collection) > 0:
        temp_copy = collection[:]
        temp_copy.pop(0)
        return 1 + estimate_length(temp_copy)
    return 0
