from flower import *

def test_petal_size_10():
    #Setup
    expected = 10, 0
    size = 10

    #Invoke
    actual = draw_petal(10)

    #Assert
    assert expected == actual

def test_petal_size_30():
    #Setup
    expected = 30, 0
    size = 30

    #Invoke
    actual = draw_petal(size)

    #Assert
    assert expected == actual

def test_petal_size_100():
    #Setup
    expected = 100, 0
    size = 100

    #Invoke
    actual = draw_petal(size)

    #Assert
    assert expected == actual

def test_draw_flower_layer_6_petals():
    #Setup
    expected = ((100, 0), (50, 86), (-49, 86), (-100, 0), (-50, -86), (49, -86))
    size = 100
    petals = 6

    #Invoke
    actual = draw_flower_layer(size, petals)

    #Assert
    assert expected == actual

def test_draw_flower_layer_5_petals():
    #Setup
    expected = ((100, 0), (30, 95), (-80, 58), (-80, -58), (30, -95))
    size = 100
    petals = 5

    #Invoke
    actual = draw_flower_layer(size, petals)

    #Assert
    assert expected == actual

def test_draw_flower_size_100_layers_5():
    #Setup
    expected = (((100, 0), (95, 29), (82, 56), (62, 78), (36, 93), (7, 99), (-22, 97), (-49, 86), (-73, 68), (-90, 43), (-98, 14), (-98, -14), (-90, -43), (-73, -68), (-50, -86), (-22, -97), (7, -99), (36, -93), (62, -78), (82, -56), (95, -29)), ((85, 0), (75, 39), (48, 69), (10, 84), (-30, 79), (-63, 56), (-82, 20), (-82, -20), (-63, -56), (-30, -79), (10, -84), (48, -69), (75, -39)), ((72, 0), (51, 51), (0, 72), (-51, 51), (-72, 0), (-51, -51), (0, -72), (51, -51)), ((61, 0), (18, 58), (-49, 36), (-49, -36), (18, -58)))
    size = 100
    layers = 5

    #invoke
    actual = draw_flower(size, layers)

    #analyze
    assert expected == actual

def test_draw_flower_size_10_layers_3():
    #Setup
    expected = (((10, 0), (7, 7), (0, 10), (-7, 7), (-10, 0), (-7, -7), (0, -10), (7, -7)), ((8, 0), (2, 8), (-6, 4), (-6, -4), (2, -8)))
    size = 10
    layers = 3

    #invoke
    actual = draw_flower(size, layers)

    #analyze
    assert expected == actual