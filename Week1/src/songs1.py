def compute():
    songs = [1, 2, 5, 4, 3]
    # add your code here to compute max
    temp = songs[0]
    for i in songs:
        if i > temp:
            temp = songs[i]
    print(temp)


if __name__ == "__main__":
    compute()
