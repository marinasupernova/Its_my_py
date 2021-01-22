# Write a function  which removes duplicates from a list.
# Write a function to find the list of words that are longer than n from a given list of words.
# Write a Python function that takes two lists and returns True if they have at least one common member.
# Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# Write a function to remove the characters which have odd index values of a given string.
# Write a Python function that takes a list of words and returns the length of the longest one.


# 
# Task 1
# my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# print(set(my_list))


# Task 2
# words = ["apple", "pear", "orange", "peach", "banana", "plum", "grapes", "kiwi"]

# filtered_words = []

# n = 5
# length = len(words)
# i = 0

# while i < length:
#     if len(words[i]) > n:
#         filtered_words.append(words[i])

#     i+=1

# print(filtered_words)


# Task 3
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7,8]

# def find_common(list1, list2):

#     intersection_set = set.intersection(set(list1),set(list2))

    
#     if len(intersection_set) > 0:
#         return True
#     else:
#         return False


# print(find_common(list1, list2))

# Task4
# string = "google.com"

# frequency = {}

# i = 0

# for letter in string:
#     if letter in frequency:
#         frequency[letter] += 1
#     else:
#         frequency[letter] = 1

# print(frequency)


# Task 5

# word = "abracadabra"

# converted_word = ""

# i = 1

# length = len(word)

# while i < length:
#     converted_word += word[i]
#     i +=2

# print(converted_word)




words = ["apple", "pear", "orange", "peach", "banana", "plum", "grapes", "kiwi", "rambutanm"]



max_word_length = len(words[0])
max_word = words[0]

length = len(words)

i = 0


while i < length:

    if len(words[i]) > max_word_length:
        max_word_length = len(words[i])
        max_word = words[i]

    i += 1


print(max_word_length)
print(max_word)







# numbers = [1, 34, 53, 3, 3455, 234]
# max_num = 1

# i = 0

# length = len(numbers)

# while i < length: 

#     if numbers[i] > max_num:
#         max_num = numbers[i]


#     i+=1

# print(max_num)