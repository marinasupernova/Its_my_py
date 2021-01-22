
def count_num_char(string):
    frequency = {}
    i = 0
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency

string = "google.com"
print(count_num_char(string))