def sum():
    result = 0
    for i in range(1, 11):
        result += i
    return result

def test_sum():
    assert sum() == 55