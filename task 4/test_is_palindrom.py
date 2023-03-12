from is_palindrom import is_palindrom


def test_1():
    assert is_palindrom('1') == True
    assert is_palindrom('12') == False
    assert is_palindrom('a') == True
    assert is_palindrom('1a') == False
    assert is_palindrom('') == True
    assert is_palindrom('aba') == True
    assert is_palindrom('aaabbbbbbaaa') == True
