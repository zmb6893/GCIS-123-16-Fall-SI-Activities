import conditionals_and_testing

def test_my_max_5_compare_2():
    #setup
    n1 = 5
    n2 = 2
    expected = 5

    #invoke
    result = conditionals_and_testing.my_max(n1, n2)

    #analyze
    assert result == expected