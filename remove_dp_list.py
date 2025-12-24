def rm_dp(l):
    rev=[]
    for i in l:
        if i not in rev:
            rev.append(i)
    return rev
def main():
    l=[1,2,2,3,4,4,5]
    print("Original list is,",l)
    print("List after removing duplicates:",rm_dp(l))
main()