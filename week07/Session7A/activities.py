"""
Session 7A: Making arrays,linear search, and timing functions
"""
import starter_code.arrays as arrays
import time
import random

def make_even_array(start, end):
    '''
    Make an array with even numbers from start to end
    '''

    total_range = (end - start)

    even_numbers = arrays.Array(int(total_range/2))

    count = 0
    for i in range(start,end):
        if i % 2 == 0:
            # add it to the array
            even_numbers[count] = i
            count += 1

    return even_numbers

def make_odd_array(start, end):
    '''
    Make an array with even numbers from start to end

    Parameters:
    :param int start: beginning of the array
    :param int end: ending of the array
    '''

    return

def print_every_nth_index(array, n):
    '''
    Print every nth index in an array. Example: array = [1,2,3,4,5,6,7] n = 2 output = [2,4,6]

    Parameters:
    :param int array: array to be printed
    :param int n: the increment to be applied to the list
    '''

    return

def linear_search(array, n):
    '''
    Search an array for the specified value using the linear search in an array

    Parameters:
    :param int array: array to be searched
    :param int n: the value to be found
    '''

    # one by one search
    for index in range(len(array)):
        if array[index] == n:
            # we found the number at index
            return index

    return

def random_array(size, seed):
    '''
    Fill an array with random numbers using the passed in seed

    Parameters:
    :param int size: size of the array
    :param int seed: seed for random
    '''

    random.seed(seed)

    array = arrays.Array(size)

    for i in range(size):
        array[i] = random.randint(1, 1000)

    return array

def main():
    array = make_even_array(6, 42)
    print(str(make_even_array(6, 42)))
    print("Found at index: " + str(linear_search(array, 10)))
    print(random_array(100, 4))

main()