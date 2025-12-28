from services import activate_user , safe_delete_user
from exceptions import UserAlreadyActiveError,UserNotFoundError,ActiveUserDeletionError
def api_activate_user(user_id):
    try:
        activate_user(user_id)
        return (200,"User Activated")
    except UserNotFoundError:
        return (404 ,"User not found")
    except UserAlreadyActiveError:
        return (400,"User already active")
    
def api_delete_user(user_id):
    try:
        safe_delete_user(user_id)
        return (200,"User deleted")
    except UserNotFoundError:
        return (404,"User not found")
    except ActiveUserDeletionError:
        return (403,"Active user cannot be deleted")

