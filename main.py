def main():
    words = []
    with open("valid-wordle-words.txt") as f:
        for x in f:
            words.append(x[:-1])
    print(words)


main()