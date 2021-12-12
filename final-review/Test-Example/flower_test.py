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

def test_draw_flower_6_petals():
    #Setup
    expected = ((100, 0), (50, 86), (-49, 86), (-100, 0), (-50, -86), (49, -86))
    size = 100
    petals = 6

    #Invoke
    actual = draw_flower(size, petals)

    #Assert
    assert expected == actual

def test_draw_flower_5_petals():
    #Setup
    expected = ((100, 0), (30, 95), (-80, 58), (-80, -58), (30, -95))
    size = 100
    petals = 5

    #Invoke
    actual = draw_flower(size, petals)

    #Assert
    assert expected == actual