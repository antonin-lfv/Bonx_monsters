from configuration.utils import *


def create_user_db():
    """users database"""
    if not exists('users.db'):
        user_db = sl.connect('users.db', check_same_thread=False)
        with user_db:
            user_db.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    email VARCHAR(50),
                    password VARCHAR(50),
                    token TEXT,
                    level INTEGER
                );
            """)
        return user_db
    else:
        return sl.connect('users.db', check_same_thread=False)


user_db = create_user_db()

# ===== monsters database
monster_db = sl.connect('monsters.db', check_same_thread=False)
