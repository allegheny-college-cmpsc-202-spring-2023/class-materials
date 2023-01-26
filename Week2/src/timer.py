import time


def compute():
    start = time.time()
    total = 0
    for i in range(1000000):
        total += i
    # wait for 3 seconds
    time.sleep(3)
    print("Sum of first 1 million numbers is:", total)
    # get the end time
    end = time.time()
    # get the execution time
    elapsed_time = end - start
    print("Execution time:", elapsed_time, "seconds")


if __name__ == "__main__":
    compute()
