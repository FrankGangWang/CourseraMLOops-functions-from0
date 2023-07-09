from hello import add


def test_add():
    assert 2 == add(1, 1)


def test_add1():
    assert 12 == add(11, 1)
