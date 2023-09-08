def idiotentest(a, b):
    return a + b


def not_tested():
    return "Pech gehabt"


def test_idiotentest():
    assert idiotentest(1, 2) == 3
