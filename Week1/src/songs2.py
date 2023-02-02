def compute():
    song_list = {
        "1": 156,
        "2": 141,
        "3": 35,
        "4": 94,
        "5": 88,
        "6": 61,
        "7": 111,
        "8": 77,
    }
    min_key = [key for key in song_list if song_list[key] == min(song_list.values())]
    min_key = str(min_key)
    # print(min_key)
    print("Song", min_key[2], ":", min(song_list.values()))


def compute2():
    song_list = {
        "1": 156,
        "2": 141,
        "3": 35,
        "4": 94,
        "5": 88,
        "6": 61,
        "7": 111,
        "8": 77,
    }
    temp = 1000
    res = 1
    for i in range(len(song_list)):
        if song_list[i] > temp:
            temp = song_list[i]
            res = i + 1
    print("Max song count", temp)
    print("Max song number", res)


def compute3():
    song_list = {
        1: 156,
        2: 141,
        3: 35,
        4: 94,
        5: 88,
        6: 61,
        7: 111,
        8: 77,
    }
    temp = song_list[1]
    # print(temp)

    for i in song_list:
        if song_list[1] <= song_list[i]:
            temp = song_list[i]
            print("Lowest value: ", temp)
    print(temp)


if __name__ == "__main__":
    compute3()
