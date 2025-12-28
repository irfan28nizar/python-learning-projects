def get_adult_names(users):
    new_l=[]
    for i in users:
        if i["age"]>=18:
            new_l.append(i['name'])

    return new_l