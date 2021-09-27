'''
Test for TDD
'''
import sample_questions

def test_did_i_pass_70():
    # setup
    expected = True
    score = 70

    # invoke
    result = sample_questions.did_i_pass(score)

    # analyze
    assert expected == result