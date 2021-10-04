def function(x):
    if (x > 10):
        raise IndexError("Index out of bounds")

def main():
    try:
        function(11)
    except FileNotFoundError:
        print("there was a file not found error here!")
    except IndexError:
        print("there is an indexerror here")
    except:
        print("there is another type of error")

main()