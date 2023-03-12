def print_even_values(collection: list):
    if len(collection) == 0:
        return

    temp_copy = collection[:]

    value = temp_copy.pop(0)
    if value % 2 == 0:
        print(value)
    print_even_values(temp_copy)
