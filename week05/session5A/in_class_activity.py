
def give_skittle(name, number):
    print("Giving " + name + " " + str(number) + " skittle(s)...\n")

def loop_example():
    skittles = 4
    skittles_eaten = 0
    while skittles_eaten < skittles:
        give_skittle(input("Who wants a skittle?\n"), 1)
        skittles_eaten += 1

loop_example()