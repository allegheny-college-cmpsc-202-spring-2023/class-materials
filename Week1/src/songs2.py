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
	print("Song", min_key[2], ":", min(song_list.values()))

if __name__ == "__main__":
    compute()
