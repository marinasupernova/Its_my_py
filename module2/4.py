Task4
string = "google.com"

frequency = {}

i = 0

for letter in string:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)