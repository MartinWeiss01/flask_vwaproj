import hashlib
from database.database import get_db
import config


class UserService():

    @staticmethod
    def verify(login, password):
        db = get_db()
        hashed_passorwd = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())
        # print(hashed_passorwd.hexdigest())

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
    def registration_user():
        db= get_db()
        db.execute(
            ' NEED A DATABASE WITH TABLE'

        )
        db.commit()