

def rmv_odd_char(word):
    
    converted_word = ""
    i = 1
    length = len(word)
    
    while i < length:
        converted_word += word[i]
        i +=2
    return converted_word


print(rmv_odd_char("abracadabra"))
print(rmv_odd_char("transmission"))
print(rmv_odd_char("abbreviation"))