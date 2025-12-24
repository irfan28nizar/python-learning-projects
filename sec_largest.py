def sec_largest(l):
    rev=[]
    for i in l:
        if i not in rev:
            rev.append(i)
    l=rev
    l.sort()
    return l[-2]
def main():
    l=[12,34,1,23,45,34,23,56,78,56]
    print("Original list is,[12,34,1,23,45,34,23,56,78,56]")
    print("Second largest elements is ", sec_largest(l))
main()