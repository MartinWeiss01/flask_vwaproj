import hashlib
from database.database import get_db
import config


class UserService():

    @staticmethod
    def verify(login, password):
        db = get_db()
        hashed_passorwd = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        user = db.execute('''
            SELECT users.id, users.login, users.is_active, user_types.role 
            FROM users 
            JOIN user_types ON (user_type_id = user_types.id)
            WHERE login = ? AND password = ?''', [login, hashed_passorwd.hexdigest()]).fetchone()
        if user:
            return user
        else:
            return None

    @staticmethod
    def register(email, password, phone, firstname, lastname):
        db = get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())
        db.execute('''
            INSERT INTO users (email, password, phone, firstname, lastname, roles_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', [email, hash.hexdigest(), phone, firstname, lastname, config.DEFAULT_ROLE_ID])
        db.commit()
        #result.lastrowid