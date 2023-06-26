from function import distance
def test_euclid_right():
    assert distance([1,1,1,],[1,1,1]) == 0


def test_euclid_false():
    assert distance([1,1,1,],[1,1,1]) == 1