l=[1,2,3,1]
def has_duplicates(l):
    if len(l) != len(set(l)):
        return True
    return False
print(has_duplicates(l))