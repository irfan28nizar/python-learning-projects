def get_active_users(users):
    new_l=[]
    for i in users:
        if i["active"]==True:
            new_l.append(i)
    return new_l