"""
Session 5A: Going over while loops and for-loops. For each function, choose to use a for-loop or while-loop for the implementation
"""

def flip_word(word):
    '''
    Return the word backwards

    Parameters:
    :param string word: the word to be flipped

    :return string flipped_word: word backwards
    '''

    count = 0
    reverse_word = ""
    for letter in word:
        # we want the first letter to be at the 
        # end of the word. How do we do that?
        reverse_word = reverse_word + word[len(word)-count-1]
        #count = count + 1
        count += 1

    return reverse_word


def count_by_2(start, end):
    '''
    Count up from start to end by twos. Return the product of the numbers. (Ex: start = 2; end = 10; result = 0,2,4,6,8,10; product = 3840)

    Parameters
    :param int end: The ending point
    :param int start: The starting point
    
    :return int product: The product of the numbers
    '''

    return

def sum_odd_numbers(start, end):
    '''
    Print the odd numbers from start to end. Return the sum of these numbers. (Ex: start = 1; end = 7; result = (1, 3, 5, 7); sum = 16)
    
    Parameters
    :param int end: The ending point
    :param int start: The starting point
    
    :return int sum: The sum of the odd numbers
    '''

    return

def subtractraction_loop(start, end, jump):
    '''
    Subtract by the jump until our number is equal to or less than the end. Return the number of times the loop ran.

    Parameters
    :param int end: the ending point
    :param int start: the starting point
    :param int jump: the amount to subtract by

    :return int loop_count: the number of times the loop ran
    '''
    return

def main():
    var = flip_word("Robert")
    print(var)

main()