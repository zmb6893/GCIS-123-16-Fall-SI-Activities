"""
Session 5A: Going over while loops and for loops
"""

import loops

# Write tests for the activities in loops.py
def test_flip_word_John():
    # Setup
    word = "John"
    expected = "nhoJ"

    # Invoke
    result = loops.flip_word(word)

    # Analyze
    assert expected == result


'''
# Quick explanation of assert: 

# this is what you might do in normal code
if (expected == result):
    test_passes()


# this is what you need to do in a test
assert expected == result
'''