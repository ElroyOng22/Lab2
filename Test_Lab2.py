import Lab2

def test_find_min_max():
    input_values = [1, 2, 3, 4, 5]
    expected_result = [1, 5]

    result = Lab2.find_min_max(input_values)
    assert result == expected_result

def test_calc_average():
    input_values = [1, 2, 3, 4, 5]
    expected_result = 3.0  # Expected result as a float

    result = Lab2.calc_average(input_values)
    assert result == expected_result

def test_calc_median_temperature():
    input_values = [1, 2, 3, 4, 5]
    expected_result = 3.0  # Expected result as a float

    result = Lab2.calc_median(input_values)
    assert result == expected_result

