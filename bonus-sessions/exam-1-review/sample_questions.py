"""
Practicum 1 Review: Functions, Turtle, Testing, Loops, Conditionals
""" 
import turtle as t
import random as r
# Let's start with making a new github branch! How would we do that?

# Use TDD for these functions

RADIUS = 100

def radians_to_degrees(radians):
    '''
    Make a function that translates radians to degrees, given radians. Use this equation: radian * (180/pi) = degrees.

    Parameters:
    :param float radians: radians to be converted to degrees

    :return float degrees: the number of degrees equivalent to radians
    '''


def did_i_pass(score):
    '''
    Make a function that takes in input for the score and returns true if 
    the score is more than or equal to 70 and false if under 70.

    :return boolean: whether or not you passed
    '''

    if(score >= 70):
        return True
    elif (score<70):
        return False

    return

def calculate_grade(score):
    '''
    Calculate the grade a student has and return the grade as A-90-100, B-80-90, C-70-80, D60-70, or O_O-less than 60

    Parameters:
    :param float score: the score of the examee (ex: 93.2)

    :return string: return the grade letter of the score
    '''

def make_emoji_with_input():
    '''
    Make a function that returns emojis for the input string. (EX: '0 O p P Q' becomes '0_-\n'O_-\np_-\nQ_q\n')   

    :return string: returns a string of emojis separated by a new line 
    '''

# Incremental Stuff Below

def draw_closed_semi(x,y,size,heading=90):
    '''
    Make a function that draws a semi circle closed at the bottom at x y with a default size of 100

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    '''
    t.goto(x,y)
    t.setheading(heading)
    t.down()
    t.circle(size*RADIUS, 180)  
    t.left(90)
    t.forward(size*RADIUS*2)

def draw_shell(x,y,size,color):
    '''
    Make a function that draws a shell at x, y, of size and shell_color. default color should be green

    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the shell
    '''
    t.color(color)
    t.begin_fill()
    draw_closed_semi(x, y, size)
    t.end_fill()
    t.up()

def draw_eye(x,y,size,eye_color):
    '''
    Make a function that draws an eye at x, y with a size and color

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the pupil
    '''
    t.goto(x+10*size, y)
    t.down()
    t.fillcolor(eye_color)
    t.begin_fill()
    t.circle(size*20)
    t.end_fill()
    t.up()

def draw_head(x,y,size,color,eye_color):
    '''
    Make a function that draws the head of the turtle. default head color should be green
    
    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the head
    '''
    t.down()
    t.setheading(90)
    t.fillcolor("green")
    t.begin_fill()
    draw_closed_semi(x+size*25, y, size*.25)
    t.end_fill()
    t.up()
    draw_eye(x+size*7, y+size*10, size*.3, eye_color)
    t.up()
    
def draw_legs(x,y,size,color):
    '''
    Make a function that draws all four legs of the turtle.

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the legs
    '''
    t.fillcolor(color)
    for leg in range(4):
        t.down()
        t.left(90)
        t.begin_fill()
        draw_closed_semi((x-50*size)-leg*50*size, y, size*.15,270)
        t.end_fill()
        t.up()
    
def draw_turtle(x,y,size,shell_color,eye_color):
    '''
    Make a function that draws a turtle. View the board.

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string shell_color: color of the turtle shell
    :param string eye_color: color of the eye
    '''
    draw_shell(x, y, size, shell_color)
    draw_head(x, y, size,shell_color,eye_color)
    draw_legs(x, y, size, "black")

def main():
    t.tracer(False)
    x = 0
    y = 0
    size = 1
    color = "green"
    eye_color = "black"
    shell_color = "green"
    draw_turtle(x, y, size, shell_color, eye_color)

    turtles = 0
    color = ["red", "green", "blue"]
    while (turtles < 100):
        draw_turtle(x, y, size, shell_color, eye_color)
        draw_turtle(r.randint(-300,300), r.randint(-300,300), r.randint(1, 30)*.1,color[r.randint(0,2)], eye_color)
        turtles += 1
    draw_turtle(20, 200, .25, "red", "yellow")
    
    input("Enter to continue")

main()