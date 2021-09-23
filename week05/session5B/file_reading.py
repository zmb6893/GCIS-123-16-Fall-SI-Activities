"""
Session 5B: File Reading activities. In class solutions. Look at print_word_by_word for an in-depth explanation of the code.
"""

def print_line_by_line(filename):
    '''
    Open a file and print each line. Between each line, print a '...'

    Parameters:
    :param string filename: the name of the file to be opened
    '''
    with open(filename) as file:
        for line in file:
            print(line)
            print("\n ...")
            
def print_character_by_character(filename):
    '''
    Open a file and print each line. Print each character in this format "(C)"

    Parameters:
    :param string filename: the name of the file to be opened
    '''
   
    with open(filename) as file:
        for line in file:
            for character in line:
                print("("+character+")")
            
def print_word_by_word(filename):
    '''
    Open a file and print each line. Print each word in the file separated by a new line

    Parameters:
    :param string filename: the name of the file to be opened
    '''

    # The variable names look a bit funky here, but that is intentional. I did this to demonstrate what this line really does:
    # Explanation:
    # Opens a file with the name filename and sets the name of the file variable to this_is_a_file. This opens the file at the
    # beginning and closes the file when it's done
    with open(filename) as this_is_a_file:
        # for every line in this_is_a_file
        for line in this_is_a_file:
            # we break apart the line into an array of words. We use split(" ") because we recognize that a space signals the
            # start of a new word. split(" ") will separate a string into smaller strings each time there is a space
            words = line.split(" ")
            # then we iterate over these words 
            for word in words:
                # so that we can print the word with a new line ('\n')
                print(word + "\n")

def make_text_emoji(filename):
    '''
    Open a file and use each character to make an emoji. (Ex:  O becomes (O_O) or P becomes (P_P). You can get more creative too). Ignore whitespace

    Parameters:
    :param string filename: the name of the file to be opened'''

    with open (filename) as file:
        for line in file:
            print(line)
            for character in line:
                if character != " ":
                    print(character+"_"+character)

def main():
    # These are our files!
    file1 = "data/o_o.txt"
    file2 = "data/who_am_I.txt"
    file3 = "data/huh.txt"
    file4 = "data/hmmm.txt"

    #print_line_by_line(file1)
    #print_character_by_character(file2)
    #print_word_by_word(file3)
    #make_text_emoji(file4)

if __name__ == "__main__":
    main()