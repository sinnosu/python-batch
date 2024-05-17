from ..domain.repositories.task_repository import TaskRepository
from ..domain.models.task import Task

class UpdateTaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def update_task_status(self, task_id: int, new_status: str):
        task = self.task_repository.get_task(task_id)
        if task:
            task.update_status(new_status)
            self.task_repository.update_task(task)
