def sum_digits(number : int):
    if number < 0:
         return sum_digits(-1 * number)
    if number > 9:
        return number % 10 + sum_digits(number // 10)
    return number
