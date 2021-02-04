ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
   "m", "n", "o", "p", "q", "r", "s", "t", "v", "u", "w", "x", "y", "z"]


def become_caesar(word, shift):

    new_word = ""

    if shift > len(ab_list):
        raise ValueError ("please enter a number under 24")

    for letter in word:
        if letter in ab_list:
            letter_index = ab_list.index(letter)

            if letter_index + shift < len(word):
                new_word += ab_list[letter_index + shift]
            else:
                new_word += ab_list[letter_index + shift - len(ab_list)] 
               
    return new_word 


print(become_caesar("mama", 23))

