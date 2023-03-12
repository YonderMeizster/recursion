def is_palindrom(string : str):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] != string [-1]:
        return False
    return is_palindrom(string[1:-1])
