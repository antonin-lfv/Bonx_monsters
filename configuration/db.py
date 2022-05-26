from configuration.config import *


def create_user_db():
    """users database"""
    if not exists('users.db'):
        user_db = sl.connect('users.db')
        with user_db:
            user_db.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    email VARCHAR(50),
                    password VARCHAR(50),
                    token TEXT,
                    level INTEGER,
                    id_deck INTEGER,
                    id_archivements INTEGER
                );
            """)
        return user_db
    else:
        return sl.connect('users.db')


# ===== monsters database
monster_db = sl.connect('monsters.db')
