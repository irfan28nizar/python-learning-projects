from db import get_user_by_id ,update_user_status , delete_user
from exceptions import UserNotFoundError , UserAlreadyActiveError , ActiveUserDeletionError
def activate_user(user_id):
    user=get_user_by_id(user_id)
    if not user:
        raise UserNotFoundError()
    else:
        if user["active"]==1:
            raise UserAlreadyActiveError()
        update_user_status(user_id,1)
        return True
        


def safe_delete_user(user_id):
    user=get_user_by_id(user_id)
    if not user:
        raise UserNotFoundError()
    else:
        if user["active"]==1:
            raise ActiveUserDeletionError()
        
        delete_user(user_id)
        return True