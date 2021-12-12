import turtle as t

def draw_petal(size, color="red"):
    t.tracer(False)
    t.color("red")
    t.pendown()
    t.begin_fill()

    tip_coord = None

    for i in range(4):
        if i == 1:
            tip_coord = int(t.xcor()), int(t.ycor())
        t.forward(size)
        t.left(90)

    t.end_fill()
    t.penup()
    return tip_coord

def draw_flower(size, petals, color="red"):
    angle = 360/petals

    tips = []

    for i in range(petals):
        tips.append(draw_petal(size, color))
        t.left(angle)
        t.goto(0,0)
        

    return tuple(tips)

def main():
    #print(draw_petal(100, "red"))
    print(draw_flower(100,5))
    input()

if __name__ == "__main__":
    main()