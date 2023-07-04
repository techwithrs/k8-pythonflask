from __init__ import conn

class User:
    def __init__(self, username):
        self.username = username

    def save(self):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username) VALUES (%s)', (self.username,))
        conn.commit()

    @staticmethod
    def get_all():
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return users

    @staticmethod
    def delete(user_id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
