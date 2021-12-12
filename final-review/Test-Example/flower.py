import turtle as t

def draw_petal(size, color="red"):
    # Prepare turtle
    t.tracer(False)
    t.color(color)
    t.pendown()
    t.begin_fill()

    # initialize a variable for the tip coordinates
    tip_coord = None

    # draws the petal
    for i in range(4):
        # records the tip
        if i == 1:
            tip_coord = int(t.xcor()), int(t.ycor())
        t.forward(size)
        t.left(90)

    # resets turtle
    t.end_fill()
    t.penup()

    # returns the coordinate of the tip
    return tip_coord

def draw_flower_layer(size, petals, color="red"):
    # determines the angle for separation between petals
    angle = 360/petals

    # list to keep track of the tips in a flower
    tips = []

    # draws the flower and adds to the list of tips
    for i in range(petals):
        tips.append(draw_petal(size, color))
        t.left(angle)
        t.goto(0,0)
        
    # return the out put as a tuple of tuples
    return tuple(tips)

def draw_flower(size, layers, color="red", alternate="pink", coords=list()):
    # base case
    if layers <= 1:
        draw_flower_layer(size, 3, color) 
        return

    # recursive call
    if (layers % 2):
        coords.append(draw_flower_layer(size, fibonacci(layers+3), color))
    else:
        coords.append(draw_flower_layer(size, fibonacci(layers+3), alternate))
    draw_flower(size*.85, layers-1, color, alternate, coords)
    return tuple(coords)

def fibonacci(n):
    # base case
    if n <= 1:
        return n
    else:
        # recursive call
        return(fibonacci(n-1) + fibonacci(n-2))

def draw_and_print_flower(size, layers, color="red", alternate="pink"):
    # draw the flower and get the coords
    coords = draw_flower(size, layers, color, alternate)[0]

    # Make a string using list comprehension and string concatenation
    string = "\n"
    [string:=(string+"\t\t"+str(coord)+"\n") for coord in coords]
    print("A red flower of size 30 is being drawn with 3 layers…\n\tLocation of each tip:"+string)

def main():
    # Example:
    print(draw_and_print_flower(100,3,"blue","violet"))
    input()

if __name__ == "__main__":
    main()