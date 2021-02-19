def createGenerator():
    i = 1
    j = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        
        yield i
        i += 1
        yield alphabet[j]
        j +=1

myGenerator = createGenerator() 


print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))