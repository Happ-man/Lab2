import Lab2

def test_find_min_max():
    expected_result=(1,6)
    test_list = [1,3,5,6,2]
    result = Lab2.find_min_max(test_list)
    assert (result == expected_result)

def test_calc_average():
    test_list = [1,3,5,6, 4.245,2]
    expected_result = 3.5408333333
    result = Lab2.calc_average(test_list)
    assert (round(result,4) == round(expected_result,4))

def test_median_temp():
    test_list = [1,3,4,5,,2]
    expected_result = 3.5
    result = Lab2.calc_median_temperature(test_list)
    assert (result == expected_result)
