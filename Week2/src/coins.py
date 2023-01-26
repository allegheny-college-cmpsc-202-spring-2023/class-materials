import time
import random

coins = []  # global variable


def scale(index):
    res = coins[index]
    return res


def generate(size):
    maximum = 100
    # maximum coin weight 100 grams
    genuine_weight = random.randint(2, maximum)
    defective_weight = random.randint(1, genuine_weight - 1)
    if genuine_weight == defective_weight:
        defective_weight = genuine_weight - 1
    defective_position = random.randint(0, size - 1)
    for i in range(0, size):
        if i != defective_position:
            coins.insert(i, genuine_weight)
    coins.insert(defective_position, defective_weight)


def detect(no_of_coins):
    pos = 0
    # add your logic here
    for i in range(no_of_coins - 1):
        for j in range(no_of_coins - 1):
            if coins[j] < coins[i]:
                pos = coins[j]
            elif coins[i] < coins[j]:
                pos = coins[i]
                temp = coins.index(pos)
        pass
    return pos, temp


def detect2(low, high):
    pos = 0
    # mid_point = len(coins) // 2
    # left = coins[:mid_point]  # until mid_point index
    # right = coins[mid_point : 2 * mid_point]
    first = range(low, (low + high) / 2)
    second = range((low + high) / 2, high)
    while len(coins) > 1:
        if high - low == 1:
            if first < second:
                return low
            else:
                return high
        else:
            if first < second:
                return detect2(low, (low + high) / 2)
            else:
                return detect2((low + high) / 2, high)


if __name__ == "__main__":
    start = time.time()
    size = 16  # number of coins is set here, can be any number in power of two's
    generate(size)
    print(coins)
    # pos = detect(size)
    pos = detect2(0, 17)
    print(f"Weight and location of the defective coin: {pos}")
    # print(type(pos))
    # print("position(starting at 1):", pos)
    # print("weight:",coins[pos-1])

    end = time.time()
    elapsed_time = end - start
    print("Execution time:", elapsed_time, "seconds")
