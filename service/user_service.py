import hashlib
from database.database import get_db
import config

class UserService():
    @staticmethod
    def verify(email, password):
        db = get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.activated,
                roles.title
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE email = ? AND password = ?
        ''', [email, hash.hexdigest()]).fetchone()
        if result:
            return result
        else:
            return None

    @staticmethod
    def register(email, password, phone, firstname, lastname):
        db = get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())
        try:
            result = db.execute('''
                INSERT INTO users (email, password, phone, firstname, lastname, roles_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', [email, hash.hexdigest(), phone, firstname, lastname, config.DEFAULT_ROLE_ID])
            db.commit()
            return result.lastrowid
        except Exception:
            #if new account is created, return user id (inserted id), else return -1
            return -1

    @staticmethod
    def get_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.activated,
                users.roles_id,
                roles.title,
                IIF(activated == 1, 'Approved', 'Waiting') as state
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
        ''').fetchall()
        return result

    @staticmethod
    def get_activated_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.activated,
                users.roles_id,
                roles.title
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE activated = 1
        ''').fetchall()
        return result
    
    @staticmethod
    def get_unactivated_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.activated,
                roles.title
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE activated = 0
        ''').fetchall()
        return result
    
    @staticmethod
    def activate_user(user_id):
        db = get_db()
        try:
            db.execute('''
                UPDATE users
                SET
                    activation = CURRENT_TIMESTAMP,
                    activated = 1
                WHERE id = ?
            ''', [user_id])
            db.commit()
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_roles():
        db = get_db()
        result = db.execute('''
            SELECT
                roles.id,
                roles.title
            FROM roles
        ''').fetchall()
        return result
    
    @staticmethod
    def set_user_role(user_id, role_id):
        db = get_db()
        try:
            db.execute('''
                UPDATE users
                SET roles_id = ?
                WHERE id = ?
            ''', [role_id, user_id])
            db.commit()
            return True
        except Exception:
            return False