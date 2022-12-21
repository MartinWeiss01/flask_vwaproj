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