def calculate_order_total(order):
    total=0
    for i in order["items"]:
        total+=i["price"]*i["qty"]
    return total