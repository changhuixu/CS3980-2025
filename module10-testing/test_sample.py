def increment_one(x):
    return x + 1


def test_increment_one_with_correct_answer():
    result = increment_one(3)
    assert result == 4
