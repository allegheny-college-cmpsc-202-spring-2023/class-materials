import time


def compute():
    value_of_n = 10
    value_of_out = 0
    for i in range(value_of_n):
        # if value_of_n - i > 0:
        value_of_out += i
    print(value_of_out)


if __name__ == "__main__":
    start = time.time()
    compute()
    end = time.time()
    # get the execution time
    elapsed_time = end - start
    print("Execution time:", elapsed_time, "seconds")
