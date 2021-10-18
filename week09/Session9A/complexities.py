"""
Time complexity activities. Go to quicksort.py for more practice.
"""
def hello():
    # What is my time complexity?
    print("hello")
    print("goodbye")

def for_loop():
    # What is my time complexity?
    for n in range(3):
        print("hello")
        print("goodbye")

def two_for_loop():
    # What is my time complexity?
    for n in range(3):
        print("hey")
    for n in range(3):
        print("bye")

def nested_for_loop():
    # What is my time complexity?
    for n in range(3):
        print("hello")
        for i in range(3):
            print("hello")
        print("goodbye")
        for i in range(3):
            print("goodbye")

def recurse(iteration = 3):
    # What is my time complexity?
    if(iteration == 0):
        return
    print("hello %d"%iteration)
    recurse(iteration-1)

def main():
    hello()
    print()
    for_loop()
    print()
    two_for_loop()
    print()
    nested_for_loop()
    print()
    recurse()

if __name__ == "__main__":
    main()