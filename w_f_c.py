s=input("Enter a string: ")
def non_rep(s):
    d={}
    for i in s:
            d[i]=d.get(i,0)+1
    for i in s:
        if d[i]==1:
            return i
print("The first non-repeating character is :",non_rep(s))