def print_even_indexes(collection : list):
    if len(collection) == 0:
        return

    print(collection[0])
    print_even_indexes(collection[2:])