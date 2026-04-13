import sys

def main():
    words = []
    with open("valid-wordle-words.txt") as f:
        for x in f:
            words.append(x[:-1])
    green_word = ["+", "+", "+", "+", "+"]
    
    while True:
        print("Input 5 letter word:")
        word_input = input()
        if word_input == "exit":
            sys.exit()
        print("Input type: g for green, y for yellow, b for black:")
        result_input = input()
        

        for i in range(0, 5):
            if result_input[i] == "b":
                for word in words[:]:
                    if word_input[i] in word:
                        words.remove(word)
            elif result_input[i] == "y":
                for word in words[:]:
                    if word_input[i] == word[i]:
                        words.remove(word)
                    if word_input[i] not in word:
                        words.remove(word)
            elif result_input[i] == "g":
                if word_input[i] == green_word[i]:
                    print("already checked")
                    continue
                for word in words[:]:
                    green_word[i] = word_input[i]
                    if word_input[i] != word[i]:
                        words.remove(word)
        chars = {}
        for word in words:
            for i in range(0, 5):
                if word[i] in chars:
                    chars[word[i]] += 1
                else:
                    chars[word[i]] = 1
        amount = len(words)
        print(f"There are {amount} words left")
        print(words)
        print(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        if amount == 1:
            sys.exit()

                

        




    


main()