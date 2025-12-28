from db import get_user_by_id ,update_user_status , delete_user

def activate_user(user_id):
    user=get_user_by_id(user_id)
    if not user:
        return "USER_NOT_FOUND"
    else:
        if user["active"]==1:
            return "ALREADY_ACTIVE"
        else:
            update_user_status(user_id,1)
            return "ACTIVATED"
        


def safe_delete_user(user_id):
    user=get_user_by_id(user_id)
    if not user:
        return"USER_NOT_FOUND"
    else:
        if user["active"]==1:
            return"CANNOT_DELETE_ACTIVE_USER"
        else:
            delete_user(user_id)
            return"DELETED"