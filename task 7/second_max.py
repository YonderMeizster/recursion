def _get_second_max(values, index, max_value, second_max):
    if index > len(values) - 1:
        return second_max
    cur_value = values[index]

    if cur_value >= max_value:
        second_max = max_value
        max_value = cur_value
    elif cur_value > second_max:
        second_max = cur_value

    return _get_second_max(values, index + 1, max_value, second_max)


def get_second_max(values : list):
    if len(values) < 2:
        raise ValueError('Not enough numbers in collection')
    max_value = max(values[:2])
    second_max = min(values[:2])
    if len(values) == 2:
        return second_max
    return _get_second_max(values, 2, max_value, second_max)


get_second_max([14, 2, 15, 16])