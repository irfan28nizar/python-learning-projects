from services import activate_user,safe_delete_user
from exceptions import UserAlreadyActiveError,UserNotFoundError,ActiveUserDeletionError
from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return {"status":"API running"}

@app.route("/users/<int:user_id>/activate",methods=["POST"])
def activate_user_api(user_id):
    try:
        activate_user(user_id)
        return {"status":"success","message":"User Activated"} , 200
    except UserNotFoundError:
        return {"status":"failed","message":"User not found"} , 404
    except UserAlreadyActiveError:
        return {"status":"failed","message":"User already active"} , 400
    
@app.route("/users/<int:user_id>",methods=["DELETE"])
def api_delete_user(user_id):
    try:
        safe_delete_user(user_id)
        return{"status":"success","message":"User deleted"},200
    except UserNotFoundError:
        return{"status":"failed","message":"User not found"},404
    except ActiveUserDeletionError:
        return{"status":"failed","message":"Active user cannot be deleted"},403
    

if __name__=="__main__":
    app.run(debug=True)
