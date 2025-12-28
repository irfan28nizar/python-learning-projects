def validate_order(order):
    if not order["items"]:
        return "INVALID"
    elif order["status"] not in ["delivered", "pending"]:
        return "INVALID"
    else:
        return "VALID"

