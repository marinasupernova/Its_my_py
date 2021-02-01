#  alphabet = dict.fromkeys(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
#                           "m", "n", "o", "p", "q", "r", "s", "t", "v", "u", "w", "x", "y", "z"], "smth")


# alphabet = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 
            # 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'u': 'u', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}



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


print(become_caesar("mama", 229))



# for i in range(0, 100):
#     print(i)
#     print(become_caesar("z", i))




# i = 0

# length = len(word)

# while i < length:
#     if 
#     i +=1

# for letter in alphabet:
#     print(letter)


    # if letter in alphabet: # если буква в ключах  ->
    #     ''' то записываем в новый список значение след буквы  '''  