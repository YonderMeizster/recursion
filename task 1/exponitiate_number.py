def exponitiate(number, power : int):
    if power == 0:
        return 1
    if power == 1:
        return number
    if power > 1:
        return number * exponitiate(number, power - 1)
    if power < 0:
        if number == 0:
            raise ZeroDivisionError('0.0 cannot be raised to a negative power')
        return 1 / (number * exponitiate(number, (-1 * power) - 1))
