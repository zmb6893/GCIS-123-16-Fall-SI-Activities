
def give_cookie(name, number):
    print("Giving " + name + " " + str(number) + " cookie(s)...\n")

def loop_example():
    cookies = 6
    cookies_eaten = 0
    while cookies_eaten < cookies:
        give_cookie(input("Who wants a cookie?\n"), 2)
        cookies_eaten += 2

loop_example()