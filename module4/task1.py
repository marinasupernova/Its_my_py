class MyIteratorFactory:
    
    i = -1
    j = -1
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def __next__(self):
        self.i += 1
        if self.i % 2:
            self.j += 1
            return self.alphabet[self.j]
        return self.i

        
myIter = MyIteratorFactory() 

# myIter = iter([1,2,3,4,5])


print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

def createGenerator():
    i = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        # solution goes here
        i += 1
        
myGenerator = createGenerator() 


print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))