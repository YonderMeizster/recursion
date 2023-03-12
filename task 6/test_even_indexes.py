from print_even_indexes import print_even_indexes


def _catch_stdout(collection, capsys):
    print_even_indexes(collection)
    captured_out = capsys.readouterr()
    return captured_out.out


def test_empty(capsys):
    assert _catch_stdout([], capsys) == ''


def test_normal(capsys):
    assert _catch_stdout([1, 2, 3, 4, 5], capsys) == '1\n3\n5\n'


def test_one_value(capsys):
    assert _catch_stdout([0], capsys) == '0\n'
