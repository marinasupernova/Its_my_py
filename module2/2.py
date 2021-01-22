
def find_word_nolonger(words):
    filtered_words = []
    n = 5
    length = len(words)
    i = 0
    while i < length:
        if len(words[i]) > n:
            filtered_words.append(words[i])
        i+=1
    return filtered_words

words = ["apple", "pear", "orange", "peach", "banana", "plum", "grapes", "kiwi"]
print(find_word_nolonger(words))