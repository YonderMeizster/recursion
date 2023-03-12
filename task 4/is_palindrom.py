def is_palindrom(string : str):
    if len(string) == 0:
        return True
    return string[0] == string [-1] and is_palindrom(string[1:-1])
