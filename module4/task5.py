'''write a class based iterator which works like linked list:

each member has link on prev and next member
if next member is empty returns stop iteration
create methods to add item in beginning of list and in end of list
create method to pop items from beginning or end

fill your list using defined methods and execute for cycle on it'''


class MyIterator:
    elements = []
    i = -1

    def __init__(self, elements):
        self.elements = elements

    def __next__(self):
        self.i += 1
        return self.elements[self.i]

    def add_tobeginning(self):
        pass

    def add_toend(self):
        pass
    
    def pop_frombeginning(self):
        pass

    def pop_fromend(self):
        pass


my_iterator = MyIterator([1,2,3,4,5,6,7,8,9])

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


