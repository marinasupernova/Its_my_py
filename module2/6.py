words = ["apple", "pear", "orange", "banana", "plum", "grapes", "rambutan"]


def max_length(words):

    max_word_length = len(words[0])
    max_word = words[0]

    length = len(words)
    i = 0

    while i < length:

        if len(words[i]) > max_word_length:
            max_word_length = len(words[i])
            max_word = words[i]
        i += 1

    return max_word_length, max_word


print(max_length(words))
