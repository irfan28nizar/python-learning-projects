def find_user_by_id(users, user_id):
    for i in users:
        if i['id']==user_id:
            return i
    return None