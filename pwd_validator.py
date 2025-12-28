def is_valid_password(pwd):
    u=0
    n=0
    for i in pwd:
        if i.isupper():
            u+=1
        if i.isdigit():
            n+=1
    if len(pwd)<8:
        return False
    elif u==0:
        return False
    elif n==0:
        return False
    else:
        return True 