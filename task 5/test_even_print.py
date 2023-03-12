from print_even_values import print_even_values


def _catch_stdout(collection, capsys):
    print_even_values(collection)
    captured_out = capsys.readouterr()
    return captured_out.out


def test_empty(capsys):
    assert _catch_stdout([], capsys) == ''


def test_normal(capsys):
    assert _catch_stdout([1, 2, 3, 4, 5], capsys) == '2\n4\n'


def test_zeros(capsys):
    assert _catch_stdout([0, 0, 0], capsys) == '0\n0\n0\n'


def test_no_even(capsys):
    assert _catch_stdout([1, 1, 1], capsys) == ''


def test_all_even(capsys):
    assert _catch_stdout([2, 4, 6], capsys) == '2\n4\n6\n'
