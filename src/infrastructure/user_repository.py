from ..domain.models.user import User
from ..domain.repositories.user_repository import UserRepository
from .db import connection_pool

class MySQLUserRepository(UserRepository):
    def get_user(self, user_id: int) -> User:
        conn = connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return User(**row) if row else None

    def update_user(self, user: User) -> None:
        conn = connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET email = %s WHERE user_id = %s",
                       (user.email, user.user_id))
        conn.commit()
        cursor.close()
        conn.close()
