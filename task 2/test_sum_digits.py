from sum_digits import sum_digits


def test_pos_and_neg():
    for number in range(-10000, 10000):
        digits = str(abs(number))
        exactly_right_sum = sum((int(digit) for digit in digits))
        assert exactly_right_sum == sum_digits(number)
