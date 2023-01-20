def compute():
    # assume total 10 tanks
    for i in range(1, 11):
        tanks = i
        turtles = tanks + 1
        # complete line 6 below by adding the right conditions inside the if block ...
        if tanks > 1 and turtles / (tanks - 1) == 2:
            print(turtles, tanks)


if __name__ == "__main__":
    compute()
