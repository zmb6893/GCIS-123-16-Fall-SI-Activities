"""
Session 7B: Recursion activities
"""

import turtle as t
import random as r

def fibonacci(n):
    '''
    Example from the recursion box
    '''
    # Make sure no terms less than 0
    if (n == 0):
        return 0
    if n == 1 or n == 2:
        return 1

    # return the sum of the previous two numbers
    return fibonacci(n-1) + fibonacci(n-2)


def add_to_previous(current, depth):
    '''
    Implement a function that continues to add it's previous value until the specified depth is reached.
    Return the value at depth

    Parameters:
    :param int current: current number
    :param int depth: when to end

    :return int
    '''

def draw_tree_branch(size, depth):
    '''
    Use turtle to draw a branch recursively.

    Parameters:
    :param int size: the scalar of the branch size
    '''

    return

def draw_flower(size, depth, petals=3):
    '''
    Use turtle to draw a flower recursively

    Parameters:
    :param int size: the scalar of the flower size
    '''
    if petals == 3:
        return 3

    t.fillcolor("yellow")
    t.fillcolor("black")

    t.setposition(0,0)
    length=size*20

    t.circle(length,180)

    for i in range(petals):
        t.circle(length, 180)
        t.right(360/petals)


    return

def binary_search(array, n, start, end):
    '''
    Implement a binary search algorithm

    Parameters:
    :param Array array: the array to be searched
    :param int n: The value to be searched for
    :param int start: The beginning index of the partition
    :param int end: The index of the end of the partition    
    '''
    # base cases
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    else:

        return 


def main():
    draw_flower(1, 10)
    input("enter")

if __name__ == "__main__":
    main()