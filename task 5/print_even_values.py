def print_even_values(collection: list):
    if len(collection) == 0:
        return

    if collection[0] % 2 == 0:
        print(collection[0])
        if len(collection) == 1:
            return

    print_even_values(collection[1:])
