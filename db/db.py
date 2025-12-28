import sqlite3
def create_user(user_id,name,email,active):
    conn=sqlite3.connect('app.db')
    cursor=conn.cursor()
    try:
        cursor.execute('insert into users(user_id,name,email,active) values(?,?,?,?)',(user_id,name,email,active))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        return False 
    finally:
        cursor.close()
        conn.close()   


def deactivate_and_delete_user(user_id):
    conn=sqlite3.connect("app.db")
    cursor=conn.cursor()
    try:
        cursor.execute("UPDATE users SET active=0 WHERE user_id=?", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        if cursor.rowcount==0:
            conn.rollback()
            return False
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


def delete_user(user_id):
    conn=sqlite3.connect("app.db")
    cursor=conn.cursor()
    try:
        cursor.execute("delete from users where user_id=?",(user_id))
        if cursor.rowcount==0:
            return False
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


def get_all_users():
    conn=sqlite3.connect("app.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    try:
        cursor.execute("select * from users")
        rows=cursor.fetchall()
        if rows:
            return [dict(row) for row in rows]
        else:
            return []
    except Exception as e :
        return []
    finally:
        cursor.close()
        conn.close()


def get_connection():
    import sqlite3
    conn=sqlite3.connect('app.db')
    return conn


def get_user_by_id(user_id):
    conn=sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()
    try:
        cursor.execute("select * from users where user_id=?",(user_id))
        user=cursor.fetchone()
        if user:
            return user
        else:
            return None
    except Exception as e:
        return None
    finally:
        cursor.close()
        conn.close()


def update_user_status(user_id,active):
    conn=sqlite3.connect('app.db')
    cursor=conn.cursor()
    try:
        cursor.execute("update users set active=? where user_id=?",(active,user_id));
        if cursor.rowcount==0:
            return False
        else:
            conn.commit()
            return True
    except Exception as e:
        conn.rollback()
        return False 
    finally:
        cursor.close()
        conn.close()   

