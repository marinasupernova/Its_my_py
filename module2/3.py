list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7,8]

def find_common(list1, list2):

    intersection_set = set.intersection(set(list1),set(list2))

    
    if len(intersection_set) > 0:
        return True
    else:
        return False


print(find_common(list1, list2))