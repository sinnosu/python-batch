from ..domain.models.task import Task
from ..domain.repositories.task_repository import TaskRepository
from .db import connection_pool

class MySQLTaskRepository(TaskRepository):
    def get_task(self, task_id: int) -> Task:
        conn = connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Task(**row) if row else None

    def update_task(self, task: Task) -> None:
        conn = connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = %s WHERE task_id = %s",
                       (task.status, task.task_id))
        conn.commit()
        cursor.close()
        conn.close()
