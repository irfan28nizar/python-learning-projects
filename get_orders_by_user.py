def get_orders_by_user(orders,user_id):
    l=[]
    for i in orders:
        if i["user_id"]==user_id:
            l.append(i)
    return l        
